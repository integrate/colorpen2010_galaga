import enemycl, playercl, levels,launcher

debug = False
paint = True

enemies = []
levels.level_1_enemie(enemies)

player = playercl.Playerc(530, 530)
lau1 = launcher.Launcher(levels.group1, [10, -10], [[371, 30], [518, 81], [558, 248], [393, 424]])
lau2 = launcher.Launcher(levels.group2, [610, 610], [[221, 30], [22, 127], [77, 408], [262, 364]])
lau3 = launcher.Launcher(levels.group3, [-10, 548], [[178, 515], [164, 327],[267,421], [262, 364]],10400)
lau4 = launcher.Launcher(levels.group4, [610, 548], [[461, 515], [370, 327],[357, 421], [432, 364]],10400)


# lau3 = launcher.Launcher(levels.group3, [-10, 548], [[178, 515], [164, 327],[267,421], [262, 364  ]])
# lau1 = launcher.Launcher(levels.group1, [10, -10], [[371, 30], [518, 81], [558, 248], [393, 424]],12307)
# lau2 = launcher.Launcher(levels.group2, [600, 570], [[221, 30], [22, 127], [77, 408], [262, 364]],41244)


print(levels.group3)
print(levels.group2)
