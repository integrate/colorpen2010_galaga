import pygame

import model
import settings

pygame.key.set_repeat(100)
pygame.time.set_timer(8889, 1500)
pygame.time.set_timer(8888, settings.emovet * 100)


def control():
    events = pygame.event.get()
    model.player.control(events)
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
        if o.type == pygame.KEYUP and o.key == pygame.K_q:
            model.paint = not model.paint
        if o.type == 8888:
            model.enemy1.moveright()
            model.draw = not model.draw
        if o.type == 8889:
            model.enemy2.moveright()
