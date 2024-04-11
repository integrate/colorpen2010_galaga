import pygame,nadpis,random,knopka

class Marshutizator():
    def __init__(self):
        self.spisok=[1,2,3,4,5,6,7,8,9,10]
        self.n1=nadpis.Nadpis(0,0,'build a way mode: ON',15,[255,254,7])
        self.rector=[]
        self.ryletka()
        self.button=knopka.Knopka(10,20,'custom/Entity/кнопка.png',self.ryletka)
    def draw(self,screen):
        for o in self.rector:
            pygame.draw.rect(screen,[255,254,7],o)
        self.n1.risyi(screen)
        self.numb.risyi(screen)
        self.button.risyem(screen)
    def ryletka(self):
        self.spisok=[1,2,3,4,5,6,7,8,9,10]
        self.rector.append(pygame.rect.Rect(random.randint(10,590),random.randint(10,590),10,10))
        for o in self.rector:
            self.numb = nadpis.Nadpis(o.x + 4, o.y + 4, str(self.spisok[0]), 20, [255, 0, 0])
            self.spisok.pop(0)
    def control_center(self,events):
        self.button.event(events)
