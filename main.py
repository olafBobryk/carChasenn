from pool import Pool
import pygame
from network import Network
from game import Game, drawState
from functions import *
from threading import Thread
import time

pygame.init()

screen = pygame.display.set_mode((24 * 10,36 * 10))

pygame.display.set_caption("carChasenn")

screen.fill((0,0,0))



pool = Pool()
global data
data = []

def action():
    while True:
        global data
        if len(data) > 1:
            pool.live()
        else:
            data.append(pool.live())

frame = 0

if __name__ == '__main__':
    Thread(target = action).start()


while True:
    # global frame
    # global record

    time.sleep(1 / 30)

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if 0 < len(data):


        drawState(screen,pygame,data[0],frame)
        
        pygame.display.update()

        frame += 1

        if frame >= len(data[0]['record']):

            frame = 0
            del data[0]







