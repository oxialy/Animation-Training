from src import game_functions as GF
from src import game_variables as GV

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS

from src.drawing_functions import draw_screen

import pygame, random
from pygame.locals import *
from random import choice, randrange


WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    selection = None
    run_main = True

    while run_main:

        draw_screen(WIN)

        GV.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_c:
                    pass
                if event.key == K_SPACE:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                #GV.DRAWLINE = not GV.DRAWLINE

                #rand_part = choice(GV.nearest_parts)
                #rand_part.pos = GV.pos

                if selection:
                    selection.selected = False

                selection = GV.nearest_parts[0]
                selection.selected = True
                selection.angle = GF.get_angle(selection.pos, GV.pos)
                size = selection.size[0]

                new_part_pos = GF.get_point_from_angle(selection.pos, selection.angle, size)

                new_part = (GF.Part(new_part_pos, (size,size)))

                GV.nearest_parts.append(new_part)


        GF.update_all_parts(GV.nearest_parts, GV.pos, GV.colA, GV.colB)

        GV.nearest_parts = GF.sort_elems(GV.nearest_parts)

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



