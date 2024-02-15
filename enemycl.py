import math_utils

import pygame, settings

pygame.init()


class Enemyc:
    def __init__(self, pyt, pyt2, x, y, timer, timer2, xmove_l, xmove_r, move_speed):
        self.timer_number = pygame.event.custom_type()
        self.timer_number2 = pygame.event.custom_type()
        self.timer_number3 = pygame.event.custom_type()
        self.timer_number4 = pygame.event.custom_type()
        pygame.time.set_timer(self.timer_number3, 25)
        pygame.time.set_timer(self.timer_number, timer)
        pygame.time.set_timer(self.timer_number2, timer2)
        pygame.time.set_timer(self.timer_number4, 25)
        self.gothere = True
        self.move_speed = move_speed
        self.screen = None

        self.image2 = pygame.image.load(pyt2)
        self.image = pygame.image.load(pyt)
        self.image2 = pygame.transform.scale(self.image2, [self.image2.get_width() * settings.dounler,
                                                           self.image2.get_height() * settings.dounler])
        self.image = pygame.transform.scale(self.image, [self.image.get_width() * settings.dounler,
                                                         self.image.get_height() * settings.dounler])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.krilia_yes_or_no = True
        self.povorot_yes_or_no = False
        self.flying_yes_or_no = False
        self.stop_krilia = False  # остановка мохания крыльев

        self.povorotik = 0

        self.image_povoroter1 = self.image
        self.image_povoroter2 = self.image2

        self.move_rect = pygame.rect.Rect(xmove_l, y, xmove_r - xmove_l, self.rect.height)
        self.ygol_povorota = 0

        self.dest_point = [x, y]
        self.going = [x, y]
        self.moving_speed=[1,2]

        self.ygol_povorota=3
        self.skorost=3
        self.plavniy_yes_or_no=False


    def paint(self, screen: pygame.Surface):
        self.screen = screen
        if self.krilia_yes_or_no == True:
            if self.povorot_yes_or_no == False:
                screen.blit(self.image, [self.rect.x, self.rect.y])
            if self.povorot_yes_or_no == True:
                screen.blit(self.image_povoroter1, [self.rect.x, self.rect.y])
        if self.krilia_yes_or_no == False:
            if self.povorot_yes_or_no == False:
                screen.blit(self.image2, [self.rect.x, self.rect.y])
            if self.povorot_yes_or_no == True:
                screen.blit(self.image_povoroter2, [self.rect.x, self.rect.y])

    def rect_remaker(self):
        ycenter = self.rect.centery
        xcenter = self.rect.centerx
        if self.krilia_yes_or_no == True:
            if self.povorot_yes_or_no == True:
                self.rect.size = self.image_povoroter1.get_size()
            if self.povorot_yes_or_no == False:
                self.rect.size = self.image.get_size()
        if self.krilia_yes_or_no == False:
            if self.povorot_yes_or_no == True:
                self.rect.size = self.image_povoroter2.get_size()
            if self.povorot_yes_or_no == False:
                self.rect.size = self.image2.get_size()
        self.rect.centerx = xcenter
        self.rect.centery = ycenter

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)
        pygame.draw.rect(screen, [0, 255, 0], self.move_rect, 3)

    def moving(self, number):
        self.animation_krilia()
        self.rect_remaker()
        self.rect.x += number

    def animation_krilia(self):

        self.krilia_yes_or_no = not self.krilia_yes_or_no

    def toolgun(self, events):

        for o in events:
            if o.type == self.timer_number:
                if self.stop_krilia == False:
                    self.modelier()
            if o.type == self.timer_number2:
                if self.povorot_yes_or_no:
                    self.plavniy_povorot()
            if o.type == self.timer_number3:
                if self.flying_yes_or_no:
                    self.flying()
            if o.type == self.timer_number4:
                if self.plavniy_yes_or_no:
                    self.plavniy_flying()


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

    def plavniy_povorot(self):
        if self.povorotik != self.ygol_povorota:
            if self.povorotik > self.ygol_povorota:
                self.povorotik -= 1
            else:
                self.povorotik += 1

            self.image_povoroter1 = pygame.transform.rotate(self.image, self.povorotik)
            self.image_povoroter2 = pygame.transform.rotate(self.image2, self.povorotik)
            self.rect_remaker()

    def povorot(self, ygol):
        self.ygol_povorota = -ygol
        self.stop_krilia = True
        self.povorot_yes_or_no = True

    def flying(self):
        if self.going != self.dest_point:
            self.moving_speed[0]=(self.dest_point[0]-self.going[0])/20
            self.moving_speed[1]=(self.dest_point[1]-self.going[1])/20
            if self.going[0] != self.dest_point[0]:
                self.going[0] += self.moving_speed[0]
            if self.going[1] != self.dest_point[1]:
                self.going[1] += self.moving_speed[1]
            self.rect_remaker()
            self.rect.centerx = self.going[0]
            self.rect.centery = self.going[1]
            print(self.rect,self.dest_point,self.going)

    def plavniy_fly(self):
        self.stop_krilia=True
        self.povorot_yes_or_no = True
        self.plavniy_yes_or_no=True


    def plavniy_flying(self):
        print(self.povorotik)
        self.povorotik+=3
        mather=math_utils.get_point_by_angle([self.rect.centerx,self.rect.centery],self.povorotik,3)
        self.rect.centerx=mather[0]
        self.rect.centery=mather[1]
        self.image_povoroter1 = pygame.transform.rotate(self.image, self.povorotik)
        self.image_povoroter2 = pygame.transform.rotate(self.image2, self.povorotik)
        self.rect_remaker()


    def mouse_pointer(self, xy):
        self.going=[self.rect.centerx ,self.rect.centery]
        self.stop_krilia = True
        self.flying_yes_or_no = True
        self.dest_point.clear()
        self.dest_point.append(xy[0])
        self.dest_point.append(xy[1])
        print(self.dest_point)

    def rovnyi(self):
        self.povorot_yes_or_no = False
        self.rect_remaker()
        self.stop_krilia = False
