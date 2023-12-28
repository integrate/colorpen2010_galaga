import pygame

import model
import settings

pygame.key.set_repeat(100)

def control():
    events = pygame.event.get()
    model.player.control(events)
    model.enemy1.toolgun(events)
    model.enemy2.toolgun(events)
    model.enemy3.toolgun(events)
    model.enemy4.toolgun(events)
    model.enemy5.toolgun(events)
    model.enemy6.toolgun(events)
    model.enemy7.toolgun(events)
    model.enemy8.toolgun(events)

    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
        if o.type == pygame.KEYUP and o.key == pygame.K_q:
            model.paint = not model.paint
