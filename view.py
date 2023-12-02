import pygame,model
screen = pygame.display.set_mode([600, 600])
def risovanie():
    pygame.display.flip()
    if model.fullscreen==False:
        screen = pygame.display.set_mode([600, 600])
    if model.fullscreen==True:
        screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

