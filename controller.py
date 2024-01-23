import random

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
            exit(9)
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
        if o.type == pygame.KEYUP and o.key == pygame.K_q:
            model.paint = not model.paint
        if o.type == pygame.KEYUP and o.key == pygame.K_d:
            model.enemies[0].povorot(random.randint(45, 180))
        if o.type == pygame.KEYUP and o.key == pygame.K_a:
            model.enemies[0].rovnyi()
        if o.type == pygame.KEYUP and o.key == pygame.K_a:
            pass