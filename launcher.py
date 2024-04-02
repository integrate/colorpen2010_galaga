import pygame,enemycl

class Launcher:
    def __init__(self,group:list,start,pyt,wait=1):
        self.waiting=group
        self.fly=[]
        self.start=start
        self.pyt=pyt
        self.launh=False
        self.pogranichnik=False

        for i in group:
            i.rect.x=-30
            i.rect.y=-30

        self.timer2=pygame.event.custom_type()
        self.timer_number = pygame.event.custom_type()

        pygame.time.set_timer(self.timer_number, 120)
        pygame.time.set_timer(self.timer2, wait)
    def flying_launh(self):
        self.launh=True
    def physical_gun(self,events):
        for o in events:
            if o.type == self.timer2:
                self.pogranichnik=True
            if o.type == self.timer_number and self.pogranichnik==True:
                self.timer()

    def timer(self):
        if self.launh==True:
            if len(self.waiting)!=0:
                self.fly.append(self.waiting[0])
                del self.waiting[0]
        if len(self.fly)!=0:
            for o in self.fly:
                o.plavniy_fly_tohcy(self.start, self.pyt)
                del self.fly[0]
