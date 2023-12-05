import pygame, model

screen = pygame.display.set_mode([600, 600])


def risovanie():
    if model.fullscreen == False and model.click == True:
        pygame.display.set_mode([600, 600])
    if model.fullscreen == True and model.click == True:
        pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
    model.player.paint(screen)
    pygame.display.flip()
