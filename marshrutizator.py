import pygame,nadpis,random,knopka,enemycl


class Marshutizator():
    def __init__(self,color= [2,2,2]):
        self.color=color
        self.n1=nadpis.Nadpis(0,0,'build a way mode: ON',15,[255,254,7])
        self.rector=[]
        self.numb=[]
        self.button=knopka.Knopka(10,20,'custom/Entity/кнопка.png',self.ryletka)
        self.ryletka()
        self.ryletka()
        self.ryletka()
        self.vidilenie=None
        self.test=enemycl.Enemyc('original/enemy/butterfly_red1.png', 'original/enemy/butterfly_red2.png', 200, 10, 500,
                                200, 200,10, 15)
    def draw(self,screen):
        for o in self.rector:
            if self.vidilenie is o:
                pygame.draw.rect(screen,[0,255,0],o)
            elif self.rector[0] is o:
                pygame.draw.rect(screen,[0,0,255],o)
            else:
                pygame.draw.rect(screen, [120, 30, 59], o)
        for i in self.numb:
            i.risyi(screen)
        self.n1.risyi(screen)
        self.button.risyem(screen)
        self.test.paint(screen)
    def ryletka(self):
        self.rectik=pygame.rect.Rect(random.randint(10,590),random.randint(10,590),10,10)
        self.rector.append(self.rectik)
        self.numb.append(nadpis.Nadpis(self.rectik.x + 4, self.rectik.y + 4, str(self.rector.index(self.rectik)), 20, [255, 0, 0]))
    def control_center(self,events):
        self.button.event(events)
        for o in events:
            for j in self.rector:
                if o.type == pygame.MOUSEBUTTONUP and j.collidepoint(o.pos):
                    self.vidilenie=j
