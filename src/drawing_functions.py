
from src import settings as sett
from src import game_variables as gv
from src import drawing_variables as dv

from .drawing_variables import bg_color, colors

import pygame
import random
from random import randrange, choice



def draw_test(win, body):
    t = gv.body[3]
    t2 = t.left_link
    t3 = t.right_link

    #pygame.draw.ellipse(win, colors['orange1'], (t2.pos, (5,5)))
    #pygame.draw.ellipse(win, colors['orange1'], (t3.pos, (5,5)))

    write_text(win, gv.pos, (sett.WIDTH - 80, 20), sett.FONT15)

    write_text(win, gv.pos, (sett.WIDTH - 80, 20), sett.FONT15)

    for i, link in enumerate(body):
        write_text(win, link.type, (630, 80 + i * 13), sett.FONT12)


def draw_screen(win):
    win.fill(bg_color)

    draw_elem(win, gv.nearest_links)
    draw_elem(win, gv.body)
    draw_elem(win, gv.body2)

    if gv.DRAWLINE:
        draw_lines(win, gv.pos, gv.nearest_links)

    gv.cursor.draw(win)
    draw_test(win, gv.body)

    pygame.draw.circle(win, colors['grey1'], (600, 527), 3)
    pygame.draw.circle(win, colors['grey1'], (600, 557), 3)
    if gv.selection:
        sel = gv.selection

        write_text(win, sel.left_link, (30, 520), sett.FONT12)
        write_text(win, sel.right_link, (30, 550), sett.FONT12)

        sel.draw_left(win)
        sel.draw_right(win)


def draw_tiles(win, tiles):
    for tile in tiles:
        tile.draw(win)

def draw_elem(win, elems):
    for elem in elems:
        elem.draw(win)

def draw_lines(win, pos, links):
    for link in links:
        link.draw_line(win, pos)

def write_text(win, data, pos, font=sett.FONT20):
    text_surf = font.render(str(data), 1, 'grey')

    win.blit(text_surf, pos)



def centered_rect(rect):
    x, y, w, h = rect

    x2 = x - w//2
    y2 = y - h//2
    new_rect = x2, y2, w, h

    return new_rect









