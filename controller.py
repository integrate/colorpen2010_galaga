import pygame

import model
import settings

pygame.key.set_repeat(100)

def control():
    events = pygame.event.get()
    model.player.control(events)
    for o in model.enemies:
        o.toolgun(events)

    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
        if o.type == pygame.KEYUP and o.key == pygame.K_q:
            model.paint = not model.paint
        if o.type == pygame.KEYUP and o.key == pygame.K_d:
            pass
        if o.type == pygame.KEYUP and o.key == pygame.K_a:
            pass
        if o.type == pygame.KEYUP and o.key == pygame.K_w:
            pass
        if o.type == pygame.KEYUP and o.key == pygame.K_s:
            pass

