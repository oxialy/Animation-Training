
from src import settings as sett
from src import game_variables as gv
from src import drawing_variables as dv

from .drawing_variables import bg_color, colors

import pygame
import random
from random import randrange, choice


class Staff:
    def __init__(self, pos):
        self.pos = pos

    def draw(self, win):

        pygame.draw.line(win, colors['lightgrey'], )


def draw_test(win):
    CX, CY = sett.WIDTH//2, sett.HEIGHT//2
    r1 = (CX, 100, 200, 30)
    r0 = centered_rect(r1)
    r2 = centered_rect((CX, 200, 200, 30))

    pygame.draw.rect(win, colors['grey1'], r0,1)
    pygame.draw.rect(win, colors['seagreen1'], r2,1)

    t = gv.body[3]
    t2 = t.left_link
    t3 = t.right_link

    pygame.draw.ellipse(win, colors['orange1'], (t2.pos, (5,5)))
    pygame.draw.ellipse(win, colors['orange1'], (t3.pos, (5,5)))

    write_text(win, gv.pos, (500,50))

    if gv.body[-1].is_clicked(gv.pos):
        write_text(win, gv.body[-1], (550, 120))

    b2 = gv.body[-2]


def draw_screen(win):
    win.fill(bg_color)

    draw_elem(win, gv.nearest_links)
    draw_elem(win, gv.body)

    if gv.DRAWLINE:
        draw_lines(win, gv.pos, gv.nearest_links)

    gv.cursor.draw(win)
    draw_test(win)


def draw_tiles(win, tiles):
    for tile in tiles:
        tile.draw(win)

def draw_elem(win, elems):
    for elem in elems:
        elem.draw(win)

def draw_lines(win, pos, links):
    for link in links:
        link.draw_line(win, pos)

def write_text(win, data, pos):
    font = pygame.font.SysFont('arial', 20)
    text_surf = font.render(str(data), 1, 'grey')

    win.blit(text_surf, pos)



def centered_rect(rect):
    x, y, w, h = rect

    x2 = x - w//2
    y2 = y - h//2
    new_rect = x2, y2, w, h

    return new_rect









