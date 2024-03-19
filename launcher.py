import pygame,enemycl

class Launcher:
    def __init__(self,group,start,pyt):
        self.group=group
        self.start=start
        self.pyt=pyt
    def flying_launh(self):
        for o in self.group:
            o.plavniy_fly_tohcy(self.start, self.pyt)