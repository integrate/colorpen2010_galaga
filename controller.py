import model
import pygame


def control():
    events = pygame.event.get()
    model.player.control(events)
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_F11:
            model.fullscreen = not model.fullscreen
        if o.type == pygame.KEYUP and o.key==pygame.K_F11:
            if model.click == True:
                model.click = False
            elif model.click == False:
                model.click = True
