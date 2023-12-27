
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

    f = gv.field

    write_text(win, round(gv.GRAVITY_INTENSITY, 2), (33,40), sett.FONT15, colors['cyan1'])
    write_text(win, gv.pos, (sett.WIDTH - 80, 20), sett.FONT15)

    pygame.draw.circle(win, colors['darkblue1'], (47,300), 10, 1)
    if gv.TOGGLE_FIELD:
        pygame.draw.circle(win, colors['lightblue1'], (47,300), 8)

    write_text(win, len(f.field), (80, 520), sett.FONT15)

    f = gv.f1.field
    w = sorted(f, key=lambda wind: wind.force[0], reverse=True)[0]

    write_text(win, w.force, (30, 520), sett.FONT15)

    for i, link in enumerate(body):
        write_text(win, link.type, (630, 80 + i * 13), sett.FONT12, colors['darkgrey1'])


def draw_screen(win):
    win.fill(bg_color)

    gv.field.draw(win)
    draw_elem(win, gv.fields)

    draw_elem(win, gv.body)

    draw_elem(win, gv.all_links)

    if gv.DRAWLINE:
        draw_lines(win, gv.pos, gv.nearest_links)

    gv.cursor.draw(win)

    draw_test(win, gv.body)

    pygame.draw.circle(win, colors['grey1'], (600, 527), 3)
    pygame.draw.circle(win, colors['grey1'], (600, 557), 3)
    if gv.selection:
        sel = gv.selection

        write_text(win, sel.left_link, (30, 620), sett.FONT12)
        write_text(win, sel.right_link, (30, 650), sett.FONT12)

        if sel.left_link:
            sel.draw_left(win)
        if sel.right_link:
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

def draw_all_bodies(win, bodies):
    for body in bodies:
        draw_elem(win, body)

def write_text(win, data, pos, font=sett.FONT20, col=colors['lightgrey1']):
    text_surf = font.render(str(data), 1, col)

    win.blit(text_surf, pos)



def centered_rect(rect):
    x, y, w, h = rect

    x2 = x - w//2
    y2 = y - h//2
    new_rect = x2, y2, w, h

    return new_rect









