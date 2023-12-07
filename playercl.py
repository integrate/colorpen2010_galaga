import pygame


class Playerc:
    def __init__(self,x,y):
        self.image = pygame.image.load('sprites/player/player_ship.png')
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def paint(self, screen: pygame.Surface):
        screen.blit(self.image, [self.rect.x,self.rect.y])

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect,3)

    def control(self, events):
        for o in events:
            if o.type == pygame.KEYDOWN and o.key == pygame.K_a:
                self.rect.x-=10
            if o.type == pygame.KEYDOWN and o.key == pygame.K_d:
                self.rect.x+=10