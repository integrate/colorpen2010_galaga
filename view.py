import model
import pygame
import settings

screen = pygame.display.set_mode(settings.screen_size)
background = pygame.image.load('custom/space.jpg')
background2 = pygame.transform.scale(background, [600, 600])


def risovanie():
    screen.blit(background2, [0, 0])

    if model.paint == True:
        for o in model.enemies:
            o.paint(screen)
        if model.build_true_or_false==True:
            model.korobka.draw(screen)
        model.player.paint(screen)
    if model.debug == True:
        for i in model.enemies:
            i.paint_debug(screen)
        model.player.paint_debug(screen)
    pygame.display.flip()
