from src import game_functions as GF
from src import game_variables as GV

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS
from src.game_variables import body, nearest_links

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
                pass


        GF.update_all_parts(GV.nearest_links, GV.pos, GV.colA, GV.colB)
        GF.update_all(body)

        GV.nearest_links = GF.sort_elems(GV.nearest_links)

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



