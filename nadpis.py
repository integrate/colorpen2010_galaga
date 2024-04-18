import pygame

pygame.init()


class Nadpis():
    def __init__(self, x, y, text, size=50, color=(55, 25, 20), background=None):

        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.background = background
        self.h = pygame.font.SysFont('arial', size, True, True)
        self.d = self.h.render(' ' + self.text, True, self.color, self.background)
    def nadpisi(self, coins):
        self.d = self.h.render(str(int(coins)) + ' ' + str(self.text), True, self.color, self.background)

    def risyi(self, screen):
        screen.blit(self.d, [self.x, self.y])

    @property
    def swet(self):
        if self.color == [255, 0, 0]:
            return 'красный'
        elif self.color == [0, 255, 0]:
            return 'зелёный'
        else:
            return 'неизвесный науке цвет'

    @swet.setter
    def swet(self, newcolor):
        if newcolor == 'красный':

            self.color = [255, 0, 0]
        elif newcolor == 'зелёный':
            self.color = [0, 255, 0]

    @property
    def chislo(self):
        return self.cifra

    @chislo.setter
    def chislo(self, zifra):
        self.cifra = zifra
        self.nadpisi(self.cifra)
