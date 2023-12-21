from src import game_functions as GF
from src import game_variables as GV

from src import settings
from src.settings import WIDTH, HEIGHT, clock, FPS

from src.drawing_functions import draw_screen

import pygame
from pygame.locals import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def initialize_grid(grid):
    i, j = GV.tile1.pos
    grid[j][i] = GV.tile1

    return grid


def main():
    run_main = True

    while run_main:

        draw_screen(WIN)

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


        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



