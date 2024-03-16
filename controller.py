import pygame

import model,levels

pygame.key.set_repeat(100)

all_points = [[100, 200], [300, 150], [126, 421]]


def control():
    events = pygame.event.get()
    model.player.control(events)
    for o in model.enemies:
        o.toolgun(events)

    for o in events:
        if o.type == pygame.QUIT:
            exit(9)

        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
        if o.type == pygame.KEYUP and o.key == pygame.K_q:
            model.paint = not model.paint
        if o.type == pygame.KEYUP and o.key == pygame.K_d:
            model.enemies[0].plavniy_fly(45, True)
        if o.type == pygame.KEYUP and o.key == pygame.K_a:
            model.enemies[0].rovnyi()
        if o.type == pygame.KEYUP and o.key == pygame.K_f:
            model.enemies[0].plavniy_fly(111, False)
        if o.type == pygame.KEYUP and o.key == pygame.K_r:
            model.enemies[0].plavniy_fly(180, False)
        if o.type == pygame.KEYUP and o.key == pygame.K_b:
            for j in levels.group1:
                j.plavniy_fly_tohcy([10,-10],[[371, 30], [518, 81], [558, 248], [393, 424]])
            for k in levels.group2:
                k.plavniy_fly_tohcy([610,610],[[221,30],[22 ,127],[77,408],[262,364]])



        if o.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            # model.enemies[0].mouse_pointer(o.pos)
