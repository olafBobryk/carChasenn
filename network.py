import copy
import enum
from random import random
from functools import reduce
import math



class Network: 
    def __init__(self,layers):

        self.net = [];
        self.gradients = [];

        if not isinstance(layers[0], list):

            for i in range(len(layers)):
                self.net.append([])

                for j in range(layers[i]):
                    self.net[i].append([])
                    self.net[i][j] = {
                        'activation': 0,
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


    def learn(self,inputs,labels):

        net = copy.deepcopy(self.net)

        net.insert(0,[{'activation': num} for num in inputs])



        for i in range(1, len(net) - 1):
            
            for j in range(len(net[i])):

                

                weighted = []

                # for idx,x in enumerate(self.net[i][j]['weights']):
                #     weighted.append(x * net[i - 1][idx]['activation'])

                weighted = [x * net[i - 1][idx]['activation'] for idx,x in enumerate(self.net[i][j]['weights'])]


                weighted = sum(weighted) + self.net[i][j]['bias']

                sigmoid = 1 / (1 + math.exp(-weighted))

                net[i][j]['activation'] = sigmoid

        # exit()


            






    def calculate(self,inputs): 
        
        activation = [[*inputs]]


        for i in range(len(self.net)):
            activation.append([])

            for j in range(len(self.net[i])):

                weighted = [x * activation[i][idx] for idx,x in enumerate(self.net[i][j]['weights'])]
                
                weighted = sum(weighted) + self.net[i][j]['bias']

                sigmoid = 1 / (1 + math.exp(-weighted))
                activation[i + 1].append(sigmoid)

        return activation[-1]
            







        