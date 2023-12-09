import pygame

import model

pygame.key.set_repeat(100)


def control():
    events = pygame.event.get()
    model.player.control(events)
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
