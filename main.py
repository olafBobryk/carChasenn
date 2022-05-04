import pygame
from network import Network
from game import Game, drawState
from functions import *



pygame.init()

screen = pygame.display.set_mode((24 * 10,36 * 10))

pygame.display.set_caption("Space Invaders")

BLUE = (0, 0, 255)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
             
     
    
pair = {
    'network': Network([864,2,3]),
    'game': Game()
}

def action():
    screen.fill((0,0,0))

    pair.get('game').nextTurn(pair.get('network'))

    drawState(screen,pygame,pair['game'].state,pair['game'].score)

    pygame.display.update()
    
    # print(g['frame'])

setInterval(1 / 2,action)







# print(g.__dict__)