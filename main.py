from src import game_functions as GF
from src import game_variables as GV

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS
from src.game_variables import body, nearest_links

from src.drawing_functions import draw_screen

import pygame, random
from pygame.locals import *
from random import choice, randrange

pygame.init()

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
                    GF.toggle_field(GV.all_winds)


            if pygame.mouse.get_pressed()[0]:
                if selection:
                    GV.cursor.start = selection.pos
                    GV.cursor.end = GV.pos
                    GV.cursor.set_force()

                    selection.vel += GV.cursor.force

                    pygame.draw.rect(WIN, 'grey', (20,20, 20,20))


            if event.type == pygame.MOUSEBUTTONDOWN:
                #GV.DRAWLINE = not GV.DRAWLINE
                if selection:
                    selection.selected = False

                GV.selection = selection = GF.check_selected(GV.all_links, GV.pos)

                if not selection:
                    selection = GF.check_selected(GV.body2, GV.pos)

                if selection:
                    selection.selected = True
                    GV.cursor.set_pos(selection.pos)

        if GV.TOGGLE_FIELD:
            GV.field.move_all(GV.WALLS)
            GF.update_fields(GV.fields, GV.WALLS)


        GF.update_all_parts(GV.nearest_links, GV.pos, GV.colA, GV.colB)
        GF.update_all(GV.body)
        GF.update_all(GV.all_links, GV.fields)

        GV.nearest_links = GF.sort_elems(GV.nearest_links)

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



