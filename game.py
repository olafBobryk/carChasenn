from math import floor
from random import random
import numpy as np
import copy

class Game():
    def __init__(self):
        self.state = [];
        self.frame = 0;
        self.score = 0;
        self.done = False;
        self.record = [];

        for x in range(24):
            self.state.append([])
            for y in range(36):
                self.state[x].append(0)

        self.state[floor(len(self.state) / 2)][len(self.state[0]) - 2] = 1

    def nextTurn(self,network):
        if self.done: return 

        
        inputs = np.array(self.state)

        inputs = inputs.ravel()

        inputs = [x / 2 for x in inputs]

        outputs = network.calculate(inputs)

        self.nextState(outputs)



    
    def nextState(self,inputs):

        def getVal(obj):
            return obj.get('val')

        dir = [{
            'dir': 'left',
            'val': inputs[0]
        },{
            'dir': 'right',
            'val': inputs[1]
        },{
            'dir': 'none',
            'val': inputs[2]
        }]

        dir = sorted(dir, key=lambda d: d['val'])[0]['dir']
        

        if self.done: 
            return
        
        new = []

        for x in range(len(self.state)):
            new.append([])
            for y in range(len(self.state[x])):
                new[x].append(0)


        for x in range(len(self.state)):
            for y in range(len(self.state[x])):
                try:
                    if self.state[x][y - 1] == 1:

                        change = {'right' : 1,'left' : -1,'none' : 0}[dir]

                        if new[x + change][y - 1] == 2:
                            self.done = True
                        elif x + change < 0 or x + change >= len(self.state[0]):
                            self.done = True
                        else:
                            new[x + change][y - 1] = self.state[x][y - 1]
                    else:
                        if not new[x][y] == 1:
                            new[x][y] = self.state[x][y - 1]
                except Exception as e:
                    self.done = True

        if self.frame % 10 == 0:
            new[floor(random() * len(self.state))][0] = 2

        self.frame += 1
        self.score += 1 

        self.state = new

        self.record.append(copy.deepcopy(self.state))





def drawState(screen,pygame,state,score):

    res = screen.get_width() / len(state)

    for x in range(len(state)):
        for y in range(len(state[x])):
            
            col = [
                (255,255,255),
                (0,0,255),
                (255,0,0)
            ][state[x][y]]

            pygame.draw.rect(screen, col, (x * res, y * res, x * res + res, y * res + res))



