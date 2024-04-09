import pygame,nadpis,random,knopka

class Marshutizator():
    def __init__(self):
        self.n1=nadpis.Nadpis(0,0,'build a way mode: ON',15,[255,254,7])
        self.rector=[]
        self.ryletka()
        self.button=knopka.Knopka(10,20,'custom/Entity/кнопка.png',self.ryletka)
    def draw(self,screen):
        for o in self.rector:
            pygame.draw.rect(screen,[255,254,7],o)
        self.n1.risyi(screen)
        self.button.risyem(screen)
    def ryletka(self):
        self.rector.append(pygame.rect.Rect(random.randint(10,590),random.randint(10,590),10,10))

    def control_center(self,events):
        self.button.event(events)
