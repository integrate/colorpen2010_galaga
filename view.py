import model
import pygame

screen = pygame.display.set_mode([600, 600])


def risovanie():
    screen.fill([0, 0, 0])
    if model.fullscreen == False and model.click == False:
        pygame.display.set_mode([600, 600])
        print(600)
    if model.fullscreen == True and model.click == True:
        pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
        print('f')
    model.player.paint(screen)
    model.player.paint_debug(screen)
    pygame.display.flip()
