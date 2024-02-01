import pygame, enemycl


def level_1_enemie(enemies):
    for i in range(170, 334, 40):
        enemy = enemycl.Enemyc('original/enemy/big_green1.png', 'original/enemy/big_green2.png', i, 100, 500, 25, i,
                               i + 120, 15)
        enemies.append(enemy)
    for i in range(112, 400, 40):
        enemy1 = enemycl.Enemyc('original/enemy/butterfly_red1.png', 'original/enemy/butterfly_red2.png', i, 150, 500,
                                200, i, i + 100, 15)
        enemies.append(enemy1)
        enemy2 = enemycl.Enemyc('original/enemy/butterfly_red1.png', 'original/enemy/butterfly_red2.png', i, 180, 500,
                                200, i, i + 100, 15)
        enemies.append(enemy2)
    for i in range(70, 440, 40):
        enemy3 = enemycl.Enemyc('original/enemy/fly_super_blue1.png', 'original/enemy/fly_super_blue2.png', i, 210, 500,
                                200, i, i + 100, 15)
        enemies.append(enemy3)
        enemy4 = enemycl.Enemyc('original/enemy/fly_super_blue1.png', 'original/enemy/fly_super_blue2.png', i, 240, 500,
                                200, i, i + 100, 15)
        enemies.append(enemy4)
