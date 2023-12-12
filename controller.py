import pygame,model,settings

pygame.key.set_repeat(100)
pygame.time.set_timer(8888,settings.emovet*1000)


def control():
    events = pygame.event.get()
    model.player.control(events)
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
