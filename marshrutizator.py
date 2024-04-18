import pygame,nadpis,random,knopka

class Marshutizator():
    def __init__(self,color= [255,254,7]):
        self.color=color
        self.n1=nadpis.Nadpis(0,0,'build a way mode: ON',15,[255,254,7])
        self.rector=[]
        self.numb=[]
        self.button=knopka.Knopka(10,20,'custom/Entity/кнопка.png',self.ryletka)
        self.ryletka()
        self.ryletka()
        self.ryletka()
        self.vidilenie=self.rector[1]
    def draw(self,screen):
        for o in self.rector:
            pygame.draw.rect(screen,self.color,o)
        for i in self.numb:
            i.risyi(screen)

        self.n1.risyi(screen)
        self.button.risyem(screen)
    def ryletka(self):
        self.rectik=pygame.rect.Rect(random.randint(10,590),random.randint(10,590),10,10)
        self.rector.append(self.rectik)
        self.numb.append(nadpis.Nadpis(self.rectik.x + 4, self.rectik.y + 4, str(self.rector.index(self.rectik)), 20, [255, 0, 0]))
    def control_center(self,events):
        self.button.event(events)
