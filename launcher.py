import pygame,enemycl

class Launcher:
    def __init__(self,group:list,start,pyt):
        self.waiting=group
        self.fly=[]
        self.start=start
        self.pyt=pyt
        self.launh=False

        self.timer_number = pygame.event.custom_type()
        pygame.time.set_timer(self.timer_number, 120)
    def flying_launh(self):
        self.launh=True
    def physical_gun(self,events):
        for o in events:
            if o.type == self.timer_number:

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
