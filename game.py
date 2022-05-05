from math import floor
from random import random
import numpy as np
import copy
import math

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

        temp = copy.deepcopy(self.state)

        index = index_2d(temp,1)

        offset = 11 - 12

        if offset < 0:
            for x in range(abs(offset)):
                temp.insert(0,[3 for i in range(len(self.state[0]))])
                del temp[-1]

        if offset > 0:
            for x in range(abs(offset)):
                temp.append([3 for i in range(len(self.state[0]))])
                del temp[0]


        
        inputs = np.array(temp)

        inputs = inputs.ravel()

        inputs = [x / 3 for x in inputs]

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

        speed = 1# math.floor(inputs[3] * 3)

        dir = sorted(dir, key=lambda d: d['val'])[0]['dir']
        

        if self.done: 
            return
        
        new = copy.deepcopy(self.state)

        for x in range(len(self.state)):
            new[x].insert(0,0)

            new[x].pop()

        index = index_2d(new,1)

        if index == None:
            self.done = True
            self.state = new

            self.record.append(copy.deepcopy(self.state))
            return
            

        new[index[0]][index[1]] = 0;
        
        change = {'right' : 1,'left' : -1,'none' : 0}[dir]


        try:
            if new[index[0] + change][index[1] - speed] == 3:
                self.done = True
            elif index[0] + change < 0 or index[0] + change >= len(self.state):
                self.done = True
            elif index[1] - speed < 0 or index[1] - speed >= len(self.state[0]):
                self.done = True
            else:
                if new[index[0] + change][index[1] - speed] == 2:
                    self.score += 35
                new[index[0] + change][index[1] - speed] = self.state[index[0]][index[1] - speed]
        except:
            self.done = True

        if self.frame % 5 == 0:
            pos = random() * (len(self.state) - 1)

            new[floor(pos + 0)][0] = 3
            new[floor(pos + 1)][0] = 3

            pos2 = random() * (len(self.state) - 1)

            while pos2 == pos or pos2 + 1 == pos or pos2 - 1 == pos:
                pos2 = random() * (len(self.state) - 1)

            new[floor(pos2 + 0)][0] = 3
            new[floor(pos2 + 1)][0] = 3


        if self.frame % 40 == 2:
            pos = random() * len(self.state)

            new[floor(pos + 0)][0] = 2


        self.frame += 1
        self.score += 1 

        self.state = new

        self.record.append(copy.deepcopy(self.state))





def drawState(screen,pygame,data,frame):

    font = pygame.font.SysFont("monospace", 15)

    

    state = data['record'][frame]
    genration = data['generation']
    net = data['network']

    res = 240 / len(state)

    for x in range(len(state)):
        for y in range(len(state[x])):
            
            col = [
                (255,255,255),
                (0,0,255),
                (0,255,0),
                (255,0,0)
            ][state[x][y]]

            pygame.draw.rect(screen, col, (x * res, y * res, x * res + res, y * res + res))

    label = font.render(str(genration) + ' ' + str(data['score']), 1, (0,0,0))
    screen.blit(label, (0,0))

    pygame.draw.rect(screen, [200,200,200], (240,0,720,360))

    for i in range(len(net[0])):
        pygame.draw.circle(screen, [10,10,10], [240 + 50,0 + 10 + i * 12.5],5);

        if math.sqrt((240 + 50 - pygame.mouse.get_pos()[0]) ** 2 + (0 + 10 + i * 12.5 - pygame.mouse.get_pos()[1]) ** 2) < 5:
            for x in range(len(state)):
                for y in range(len(state[x])):

                    col = net[0][i]['weights'][x * 36 + y]

                    if col < 0:
                        col = (255 * abs(col),0,0)
                    elif col > 0:
                        col = (0,255 * abs(col),0)
                    else: 
                        col = (0,0,0)

                    s = pygame.Surface((res,res))
                    s.set_alpha(128)                # alpha level
                    s.fill(col)           # this fills the entire surface
                    screen.blit(s, (x * res, y * res)) 


                    # pygame.draw.rect(screen, col, (x * res, y * res, x * res + res, y * res + res))







def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
    return None


