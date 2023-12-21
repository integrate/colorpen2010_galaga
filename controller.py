import pygame

import model
import settings

pygame.key.set_repeat(100)

def control():
    events = pygame.event.get()
    model.player.control(events)
    model.enemy2.toolgun(events)
    model.enemy1.toolgun(events)
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
        if o.type == pygame.KEYUP and o.key == pygame.K_q:
            model.paint = not model.paint
