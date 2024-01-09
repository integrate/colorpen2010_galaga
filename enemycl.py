import pygame

import settings

pygame.init()


class Enemyc:
    def __init__(self, pyt, pyt2, x, y, timer, timer2, xmove_l, xmove_r, move_speed):
        self.timer_number = pygame.event.custom_type()
        self.timer_number2 = pygame.event.custom_type()
        pygame.time.set_timer(self.timer_number, timer)
        pygame.time.set_timer(self.timer_number2, timer2)
        self.gothere = True
        self.move_speed = move_speed

        self.image2 = pygame.image.load(pyt2)
        self.image = pygame.image.load(pyt)
        self.image2 = pygame.transform.scale(self.image2, [self.image2.get_width() * settings.dounler,
                                                           self.image2.get_height() * settings.dounler])
        self.image = pygame.transform.scale(self.image, [self.image.get_width() * settings.dounler,
                                                         self.image.get_height() * settings.dounler])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.draw = True

        self.image_2 = self.image
        self.image2_2 = self.image_2

        self.move_rect = pygame.rect.Rect(xmove_l, y, xmove_r - xmove_l, self.rect.height)

    def paint(self, view, screen: pygame.Surface):
        self.screen = screen
        if view == False:
            if self.draw == True:
                screen.blit(self.image, [self.rect.x, self.rect.y])
            if self.draw == False:
                screen.blit(self.image2, [self.rect.x, self.rect.y])
        if view == True:
            if self.draw == True:
                screen.blit(self.image_2, [self.rect.x, self.rect.y])
            if self.draw == False:
                screen.blit(self.image2_2, [self.rect.x, self.rect.y])

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
        pygame.draw.rect(screen, [0, 255, 0], self.move_rect, 3)

    def moving(self, number):
        self.drawler()
        self.rect_remaker()
        self.rect.x += number

    def drawler(self):
        self.draw = not self.draw

    def toolgun(self, events):
        for o in events:
            if o.type == self.timer_number:
                self.modelier()
            if o.type == self.timer_number2:
                self.povorot(True, False, 45)

    def modelier(self):
        if self.gothere == True:
            self.moving(-self.move_speed)
        elif self.gothere == False:
            self.moving(self.move_speed)
        if self.rect.right >= self.move_rect.right:
            self.gothere = True
            self.rect.right = self.move_rect.right
        elif self.rect.left <= self.move_rect.left:
            self.gothere = False
            self.rect.left = self.move_rect.left

    def povorot(self, a, b, ygol):
        if a == True and b == True:
            self.image_2 = pygame.transform.rotate(self.image, ygol)
        if a == True and b == True:
            self.image2_2 = pygame.transform.rotate(self.image2, ygol)
