from src import game_functions as GF
from src import game_variables as GV

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS
from src.game_variables import body, nearest_links

from src.drawing_functions import draw_screen

import pygame, random, math
from pygame.locals import *
from random import choice, randrange
from math import pi

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def invert_gravity(bodies):
    for body in bodies:
        body[0].angle = -body[0].angle

    GV.GRAVITY_INTENSITY = -GV.GRAVITY_INTENSITY


def main():
    selection = None
    run_main = True

    GF.toggle_field(GV.all_winds)

    pygame.time.wait(200)

    while run_main:

        draw_screen(WIN)

        GV.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_a:
                    GF.toggle_angle(GV.all_links)
                if event.key == K_g:
                    invert_gravity(GV.grass_field)
                if event.key == K_SPACE:
                    GF.toggle_field(GV.all_winds)

            if event.type == pygame.MOUSEBUTTONDOWN:
                #GV.DRAWLINE = not GV.DRAWLINE
                if selection:
                    selection.SELECTED = False

                GV.selection = selection = GF.check_selected(GV.all_links, GV.pos)

                if not selection:
                    selection = GF.check_selected(GV.body2, GV.pos)

                if selection:
                    selection.SELECTED = True
                    GV.cursor.set_pos(selection.pos)
                    GV.cursor.set_force()

        if pygame.mouse.get_pressed()[0]:
            if selection:
                GV.cursor.start = selection.pos
                GV.cursor.end = GV.pos
                GV.cursor.set_force()

                #selection.vel += GV.cursor.force

                pygame.draw.rect(WIN, 'grey', (20,20, 20,20))
        else:
            if selection:
                GV.cursor.shorten()
                GV.cursor.set_force()

        if GV.TOGGLE_FIELD:
            GV.field.move_all(GV.WALLS)
            GF.update_fields(GV.fields, GV.WALLS)

        if selection:
            selection.vel += GV.cursor.force


        GF.update_all_parts(GV.nearest_links, GV.pos, GV.colA, GV.colB)
        GF.update_all(GV.body)
        GF.update_all(GV.all_links, GV.fields, GV.GRAVITY_INTENSITY)

        GV.nearest_links = GF.sort_elems(GV.nearest_links)

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



