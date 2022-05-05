import enum
from random import random
from functools import reduce
import math



class Network: 
    def __init__(self,layers):

        self.net = [];

        if not isinstance(layers[0], list):

            for i in range(len(layers)):
                self.net.append([])

                for j in range(layers[i]):
                    self.net[i].append([])
                    self.net[i][j] = {
                        'weights': [],
                        'bias': random() * 2 - 1
                    }

                    if i == 0:
                        continue

                    for c in range(layers[i - 1]):
                        self.net[i][j]['weights'].append(random() * 2 - 1)
            
            del self.net[0]

        else:

            self.net = layers

    def calculate(self,inputs): 
        
        activation = [[*inputs]]


        for i in range(len(self.net)):
            activation.append([])

            for j in range(len(self.net[i])):

                def weightedSum(x,idx):
                    return x * activation[i][idx]

                weighted = [x * activation[i][idx] for idx,x in enumerate(self.net[i][j]['weights'])]


                def add(a,b):
                    a + b

                
                weighted = sum(weighted) + self.net[i][j]['bias']

                sigmoid = 1 / (1 + math.exp(-weighted))
                activation[i + 1].append(sigmoid)

        return activation[-1]
            







        