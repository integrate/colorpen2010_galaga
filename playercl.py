import pygame

import settings


class Playerc:
    def __init__(self, x, y):
        image = pygame.image.load('original/player/player.png')
        self.image=pygame.transform.scale(image,[image.get_width()*settings.dounler,image.get_height()*settings.dounler])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def paint(self, screen: pygame.Surface):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)

    def control(self, events):
        for o in events:
            self.rect.centerx = pygame.mouse.get_pos()[0]
