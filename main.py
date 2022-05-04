from pool import Pool
import pygame
from network import Network
from game import Game, drawState
from functions import *

pool = Pool()

# pair = {
#     'network': Network([864,2,3]),
#     'game': Game()
# }

def action():
    pool.live();
    # pair.get('game').nextTurn(pair.get('network'))


setInterval(1 / 2,action)








# pygame.init()

# screen = pygame.display.set_mode((24 * 10,36 * 10))
# clock = pygame.time.Clock()

# pygame.display.set_caption("carChasenn")

# screen.fill((0,0,0))
    
# pair = {
#     'network': Network([864,2,3]),
#     'game': Game()
# }

# def action():
#     screen.fill((0,0,0))

#     pair.get('game').nextTurn(pair.get('network'))

#     drawState(screen,pygame,pair['game'].state,pair['game'].score)
    
#     # print(g['frame'])



# while True:
#     print(1)
#     clock.tick(3)
#     print(2)

#     action()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit()


#     action()

#     pygame.display.update()



