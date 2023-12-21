import pygame

import settings
pygame.init()

class Enemyc:
    def __init__(self, pyt, pyt2, x, y,timer):
        self.timer_number=pygame.event.custom_type()
        pygame.time.set_timer(self.timer_number,timer)


        self.image2 = pygame.image.load(pyt2)
        self.image = pygame.image.load(pyt)
        self.image2 = pygame.transform.scale(self.image2, [self.image2.get_width() * settings.dounler,
                                                           self.image2.get_height() * settings.dounler])
        self.image = pygame.transform.scale(self.image, [self.image.get_width() * settings.dounler,
                                                         self.image.get_height() * settings.dounler])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.draw=True

    def paint(self, screen: pygame.Surface):
        if self.draw == True:
            screen.blit(self.image, [self.rect.x, self.rect.y])
        if self.draw == False:
            screen.blit(self.image2, [self.rect.x, self.rect.y])
    def rect_remaker(self):
        if self.draw == True:
            ycenter = self.rect.centery
            xcenter = self.rect.centerx
            self.rect.width = self.image.get_width()
            self.rect.height = self.image.get_height()
            self.rect.centerx = xcenter
            self.rect.centery = ycenter
        if self.draw == False:
            ycenter = self.rect.centery
            xcenter = self.rect.centerx
            self.rect.width = self.image2.get_width()
            self.rect.height = self.image2.get_height()
            self.rect.centerx = xcenter
            self.rect.centery = ycenter

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)

    def moveright(self):
        self.rect.x += 15
        self.drawler()
        self.rect_remaker()

    def drawler(self):
        self.draw= not self.draw

    def toolgun(self,events):
        for o in events:
            if o.type == self.timer_number:
                self.moveright()

