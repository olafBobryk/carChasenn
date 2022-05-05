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
data = False

def action():
    while True:
        global data
        if data:
            pool.live(data)
        else:
            data = pool.live(data)

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
    if data:


        drawState(screen,pygame,data,frame)
        
        pygame.display.update()

        frame += 1

        if frame >= len(data['record']):
            frame = 0
            data = False


setInterval(1 / 2,action=show)






