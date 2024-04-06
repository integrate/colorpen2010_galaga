import pygame,nadpis

class Marshutizator():
    def __init__(self):
        self.n1=nadpis.Nadpis(0,0,'build a way mode: ON',15,[255,254,7])
    def draw(self,screen):
        self.n1.risyi(screen)