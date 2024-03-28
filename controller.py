import pygame

import model, levels

pygame.key.set_repeat(100)

all_points = [[100, 200], [300, 150], [126, 421]]

def control():
    events = pygame.event.get()

    model.player.control(events)

    model.lau1.physical_gun(events)
    model.lau2.physical_gun(events)
    model.lau3.physical_gun(events)
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
            model.lau1.flying_launh()
            model.lau2.flying_launh()
            model.lau3.flying_launh()




        # group1 [10, -10], [[371, 30], [518, 81], [558, 248], [393, 424]]
        # group2 [610, 610], [[221, 30], [22, 127], [77, 408], [262, 364]]

        if o.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            # model.enemies[0].mouse_pointer(o.pos)
