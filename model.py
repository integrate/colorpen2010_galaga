import enemycl, playercl, levels,launcher

debug = False
paint = True

enemies = []
levels.level_1_enemie(enemies)

points=levels.zercalo([[178, 515], [164, 327],[267,421], [262, 364]],600)
points2=levels.zercalo([[371, 30], [518, 81], [558, 248], [393, 424]],600)


player = playercl.Playerc(530, 530)
lau1 = launcher.Launcher(levels.group1, [10, -10], [[371, 30], [518, 81], [558, 248], [393, 424]])
lau2 = launcher.Launcher(levels.group2, [610, 610], points2)
lau3 = launcher.Launcher(levels.group3, [-10, 548], [[178, 515], [164, 327],[267,421], [262, 364]],10400,-90)
lau4 = launcher.Launcher(levels.group4, [610, 548],points,10400,90)


# lau3 = launcher.Launcher(levels.group3, [-10, 548], [[178, 515], [164, 327],[267,421], [262, 364  ]])
# lau1 = launcher.Launcher(levels.group1, [10, -10], [[371, 30], [518, 81], [558, 248], [393, 424]],12307)
# lau2 = launcher.Launcher(levels.group2, [600, 570], [[221, 30], [22, 127], [77, 408], [262, 364]],41244)