import pygame, settings,launcher,math_utils

pygame.init()


def vibor_ygol(angle_point, povorotik):
    povorotik=-povorotik
    angle_point=-angle_point
    angle_pointm1 = angle_point - 360
    angle_pointm2 = angle_point - 360*2
    angle_pointp1 = angle_point + 360
    angle_pointp2 = angle_point + 360*2
    s = [abs(angle_pointm2 - povorotik), abs(angle_pointm1 - povorotik), abs(angle_point - povorotik),
         abs(angle_pointp1 - povorotik), abs(angle_pointp2 - povorotik)]
    s1 = min(s)

    # print("куда смотрю:", povorotik, "  куда нужно:", angle_point, "   все варианты:", s, "   выбрал:", s1)

    if s1 == s[0]:
        angle_point = angle_pointm2
    elif s1==s[1]:
        angle_point = angle_pointm1
    elif s1 == s[3]:
        angle_point = angle_pointp1
    elif s1 == s[4]:
        angle_point = angle_pointp2

    return -angle_point

class Enemyc:
    def __init__(self, pyt, pyt2, x, y, timer, timer2, xmove_l, xmove_r, move_speed):
        self.timer_number = pygame.event.custom_type()
        self.timer_number2 = pygame.event.custom_type()
        self.timer_number3 = pygame.event.custom_type()
        self.timer_number4 = pygame.event.custom_type()

        pygame.time.set_timer(self.timer_number3, 25)
        pygame.time.set_timer(self.timer_number, timer)
        pygame.time.set_timer(self.timer_number2, timer2)
        pygame.time.set_timer(self.timer_number4, 20)

        self.gothere = True
        self.move_speed = move_speed
        self.screen = None

        self.group=None

        self.image2 = pygame.image.load(pyt2)
        self.image = pygame.image.load(pyt)
        self.image2 = pygame.transform.scale(self.image2, [self.image2.get_width() * settings.dounler,
                                                           self.image2.get_height() * settings.dounler])
        self.image = pygame.transform.scale(self.image, [self.image.get_width() * settings.dounler,
                                                         self.image.get_height() * settings.dounler])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.rect_start=self.rect.center
        self.krilia_yes_or_no = True
        self.povorot_yes_or_no = False
        self.image_povorot_yes_or_no = False
        self.flying_yes_or_no = False
        self.stop_krilia = True  # остановка мохания крыльев

        self.povorotik = 0

        self.ygol = 90
        self.storona = False



        self.pf_point = []

        self.image_povoroter1 = self.image
        self.image_povoroter2 = self.image2

        self.move_rect = pygame.rect.Rect(xmove_l, y, xmove_r - xmove_l, self.rect.height)
        self.ygol_povorota = 0

        self.dest_point = [x, y]
        self.going = [x, y]
        self.moving_speed = [1, 2]

        self.ygol_povorota = 3
        self.skorost = 3
        self.plavniy_yes_or_no = False
        self.plavniy_tourch_yes_or_no = False

    def paint(self, screen: pygame.Surface):
        self.screen = screen
        if self.krilia_yes_or_no == True:
            if self.image_povorot_yes_or_no == False:
                screen.blit(self.image, [self.rect.x, self.rect.y])
            if self.image_povorot_yes_or_no == True:
                screen.blit(self.image_povoroter1, [self.rect.x, self.rect.y])
        if self.krilia_yes_or_no == False:
            if self.image_povorot_yes_or_no == False:
                screen.blit(self.image2, [self.rect.x, self.rect.y])
            if self.image_povorot_yes_or_no == True:
                screen.blit(self.image_povoroter2, [self.rect.x, self.rect.y])

    def rect_remaker(self):
        """
        система хитбоксов
        """
        ycenter = self.rect.centery
        xcenter = self.rect.centerx
        if self.krilia_yes_or_no == True:
            if self.image_povorot_yes_or_no == True:
                self.rect.size = self.image_povoroter1.get_size()
            if self.image_povorot_yes_or_no == False:
                self.rect.size = self.image.get_size()
        if self.krilia_yes_or_no == False:
            if self.image_povorot_yes_or_no == True:
                self.rect.size = self.image_povoroter2.get_size()
            if self.image_povorot_yes_or_no == False:
                self.rect.size = self.image2.get_size()
        self.rect.centerx = xcenter
        self.rect.centery = ycenter

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)
        pygame.draw.rect(screen, [0, 255, 0], self.move_rect, 3)
        for o in self.pf_point:
            pygame.draw.circle(screen,[240,23,150],o,4)

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
                if self.plavniy_tourch_yes_or_no == True:
                    self.plavniy_flying_tohcy()

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

            self.povoroters()

    def povorot(self, ygol):
        self.ygol_povorota = -ygol
        self.stop_krilia = True
        self.povorot_yes_or_no = True
        self.image_povorot_yes_or_no = True

    def flying(self):
        if self.going != self.dest_point:
            self.moving_speed[0] = (self.dest_point[0] - self.going[0]) / 20
            self.moving_speed[1] = (self.dest_point[1] - self.going[1]) / 20
            if self.going[0] != self.dest_point[0]:
                self.going[0] += self.moving_speed[0]
            if self.going[1] != self.dest_point[1]:
                self.going[1] += self.moving_speed[1]
            self.rect_remaker()
            self.rect.centerx = self.going[0]
            self.rect.centery = self.going[1]

    def _idi_vperiod(self):
        mather = math_utils.get_point_by_angle([self.rect.centerx, self.rect.centery], self.povorotik, 5)
        self.rect.centerx = mather[0]
        self.rect.centery = mather[1]

    def plavniy_fly(self, ygol, storona):
        self.ygol = ygol
        self.storona = storona
        self.stop_krilia = True
        self.image_povorot_yes_or_no = True
        self.plavniy_yes_or_no = True

    def plavniy_flying(self):
        if self.povorotik != self.ygol:
            if self.storona == False:
                self.povorotik += 3
            else:
                self.povorotik -= 3
            self._idi_vperiod()
            self.povoroters()
            self.ygol_reset()

    def plavniy_fly_tohcy(self,teleport_point,pyt_tochek,ygol=180):
        # self.rect.centery=random.randint(610,650)
        self.povorotik=ygol
        self.pf_point=pyt_tochek.copy()
        self.pf_point.append(self.rect_start)
        self.stop_krilia = True
        self.rect.center=teleport_point
        self.image_povorot_yes_or_no = True
        self.plavniy_tourch_yes_or_no= True

    def plavniy_flying_tohcy(self):
        if len(self.pf_point) == 0:
            self.plavniy_tourch_yes_or_no=False
            self.rect.center=self.rect_start
            self.povorotik=0
            self.povoroters()
            return
        point=self.rect.collidepoint(self.pf_point[0])
        if point==False:
            self._idi_vperiod()
            self.povorathivay()
            self.teleport()
        else:
            del self.pf_point[0]

    def teleport(self):
        if self.rect.centery >= 650:
            self.rect.centery = -10
        elif self.rect.centery <= -50:
            self.rect.centery = 610
        if self.rect.centerx >= 650:
            self.rect.centerx = -10
        elif self.rect.centerx <= -50:
            self.rect.centerx = 610



    def povorathivay(self):
        angle_point = math_utils.get_angle_by_point([self.rect.centerx, self.rect.centery], self.pf_point[0])
        angle_point=vibor_ygol(angle_point,self.povorotik)
        if angle_point != None:
            self.povoroters()
            if self.povorotik < angle_point:
                self.povorotik += 3
            elif self.povorotik > angle_point:
                self.povorotik -= 3

    def ygol_reset(self):
        self.povorotik = self.povorotik % 360

    def povoroters(self):
        self.image_povoroter1 = pygame.transform.rotate(self.image, self.povorotik)
        self.image_povoroter2 = pygame.transform.rotate(self.image2, self.povorotik)
        self.rect_remaker()

    def mouse_pointer(self, xy):
        self.going = [self.rect.centerx, self.rect.centery]
        self.stop_krilia = True
        self.flying_yes_or_no = True
        self.dest_point.clear()
        self.dest_point.append(xy[0])
        self.dest_point.append(xy[1])

    def rovnyi(self):
        self.povorot_yes_or_no = False
        self.image_povorot_yes_or_no = False
        self.rect_remaker()
        self.stop_krilia = False
