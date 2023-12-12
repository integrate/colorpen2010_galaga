import pygame

import model

screen = pygame.display.set_mode([600, 600])
background=pygame.image.load('sprites/space.jpg')
background2=pygame.transform.scale(background,[600,600])

def risovanie():
    screen.blit(background2,[0,0])
    model.enemy1.paint(screen)
    model.enemy2.paint(screen)
    model.player.paint(screen)
    if model.debug == True:
        model.enemy1.paint_debug(screen)
        model.enemy2.paint_debug(screen)
        model.player.paint_debug(screen)
    pygame.display.flip()
