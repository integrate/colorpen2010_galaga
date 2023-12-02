import pygame, model


def control():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_F11:
            model.fullscreen = not model.fullscreen
