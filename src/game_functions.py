from src import drawing_variables as dv
from src import settings as sett

from .drawing_variables import colors

import pygame
import math
from math import sqrt, sin, cos, atan2


class Part:
    def __init__(self, pos, size, angle=0):
        self.pos = pos
        self.size = size
        self.angle = 0

        self.col = '#808080'
        self.col2 = '#909000'

        self.distance_from_mouse = 0
        self.selected = False

    def draw(self, win):
        w, h = self.size

        x = self.pos[0] - w // 2
        y = self.pos[1] - h // 2

        pygame.draw.ellipse(win, self.col, (x,y,w,h))
        if self.selected:
            pygame.draw.ellipse(win, colors['grey1'], (x,y,w,h))

    def draw_line(self, win, pos):
        pygame.draw.line(win, self.col2, self.pos, pos)

    def update_color(self, colA, colB):
        color_index = int(self.distance_from_mouse * 200 / 500)
        color_index = min(200, color_index)

        self.col = colA[color_index]
        self.col2 = colB[color_index]


    def update_distance(self, pos):
        self.distance_from_mouse = get_dist(self.pos, pos)


def update_parts_color(parts, colA):
    for part in parts:
        color_index = part.distance_from_mouse * 200 // 500
        color_index = min(250, color_index)

        part.col = colA[color_index]

def update_all_distances(parts, pos):
    for part in parts:
        pass

def update_all_parts(parts, pos, colA, colB):
    for part in parts:
        part.update_distance(pos)
        part.update_color(colA, colB)

def get_nearest_elem(pos, all_elems):
    sorted_elems = []

    for elem in all_elems:
        pass

def sort_elems(all_elems):

    return sorted(all_elems, key= lambda elem: elem.distance_from_mouse)


def get_dist(A, B):
    x1, y1 = A
    x2, y2 = B

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_angle(A, B):
    x1, y1 = A
    x2, y2 = B

    return atan2((y2-y1), (x2-x1))


def get_point_from_angle(pos, angle, dist):
    x1, y1 = pos

    a = sin(angle) / cos(angle)
    b = y1 / a * x1

    x2 = x1 + cos(angle) * dist
    y2 = y1 + sin(angle) * dist

    return x2, y2





