import pygame


class Playerc:
    def __init__(self):
        self.image = pygame.image.load('sprites/player/player_ship.png')
        self.x=300

    def paint(self, screen: pygame.Surface):
        screen.blit(self.image, [300, 300])
    def control(self,events):
        for o in events:
            if o.type ==pygame.KEYDOWN and o.key==pygame.K_w:
                pass
