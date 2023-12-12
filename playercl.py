import pygame


class Playerc:
    def __init__(self, x, y):
        image = pygame.image.load('images/player/player.png')
        self.image=pygame.transform.scale(image,[15*4,16*4])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def paint(self, screen: pygame.Surface):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)

    def control(self, events):
        for o in events:
            self.rect.centerx = pygame.mouse.get_pos()[0]
