from src import drawing_variables as DV

from src import game_functions as GF
from src import game_variables as GV
#from src import link
#from src import field

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS
from src.game_variables import body, nearest_links
from src.link import toggle_angle, check_selected
from src.field import toggle_field, update_fields, toggle_show_field

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

    toggle_field(GV.all_winds)
    GV.TOGGLE_FIELD = not GV.TOGGLE_FIELD

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
                    toggle_angle(GV.all_links)

                if event.key == K_g:
                    invert_gravity(GV.grass_field + [GV.body])

                if event.key == K_h:
                    toggle_show_field(GV.all_winds)

                if event.key == K_SPACE:
                    toggle_field(GV.all_winds)
                    GV.TOGGLE_FIELD = not GV.TOGGLE_FIELD


            if event.type == pygame.MOUSEBUTTONDOWN:
                #GV.DRAWLINE = not GV.DRAWLINE
                if selection:
                    selection.SELECTED = False

                GV.selection = selection = check_selected(GV.all_links, GV.pos)

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


        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            GV.GRAVITY_INTENSITY += 0.01


        elif keys[K_DOWN]:
            GV.GRAVITY_INTENSITY -= 0.01

        elif keys[K_LEFT]:
            GV.GRAVITY_INTENSITY = 0.02

        elif keys[K_RIGHT]:
            GV.GRAVITY_INTENSITY = -0.17


        if selection:
            selection.vel += GV.cursor.force

        GV.cursor.shorten()
        GV.cursor.set_force()


        GV.field.move_all(GV.WALLS)
        update_fields(GV.fields, GV.WALLS)

        GF.update_all_parts(GV.nearest_links, GV.pos, GV.colA, GV.colB)
        GF.update_all(GV.body)
        GF.update_all(GV.all_links, GV.fields, GV.GRAVITY_INTENSITY)

        GV.nearest_links = GF.sort_elems(GV.nearest_links)

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



