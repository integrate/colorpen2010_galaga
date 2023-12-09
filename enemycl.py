import pygame


class Enemyc:
    def __init__(self, pyt, x, y):
        self.image = pygame.image.load(pyt)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def paint(self, screen: pygame.Surface):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)
