import math
from random import random
from game import Game
from network import Network
import copy


class Pool():
    def __init__(self):
        self.population = [];
        self.generation = 0;

        for i in range(30):
            self.population.append({
                'game': Game(),
                'network': Network([864,1,3])
            })


    def live(self):
        while True:
            done = True

            for i in self.population:

                if i['game'].done: 
                    continue

                i['game'].nextTurn(i['network']) 

                if not i['game'].done: done = False

            if done: break

        return self.nextGeneration();

    def nextGeneration(self):

        self.population = sorted(self.population, key=lambda d: d['game'].score) 
        self.population.reverse()

        record = self.population[0]['game'].record
        score =  self.population[0]['game'].score
        network = self.population[0]['network'].net

        nextPopulation = [];

        frac = 50

        for i in range(len(self.population)):
            if i < math.ceil(len(self.population)):
                nextPopulation.append({
                    'game': Game(),
                    'network': Network(self.population[i]['network'].net)
                })
            else:
                pos = i - math.ceil(len(self.population) / 2)
                net = copy.deepcopy(self.population[pos]['network'].net)

                for layer in net:
                    for node in layer:
                        node['weights'] = [val + (random() - 0.5) / frac for val in node['weights']]
                        node['bias'] += (random() - 0.5) / frac

                nextPopulation.append({
                    'game': Game(),
                    'network': Network(net)
                })

        self.generation += 1
        self.population  = nextPopulation

        return {
            'record': record,
            'generation': self.generation,
            'score': score,
            'network': network
        }



            