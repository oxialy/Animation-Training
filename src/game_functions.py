from src import drawing_variables as dv
from src import settings as sett

from .drawing_variables import colors

import pygame
import math
from pygame import Vector2
from math import sqrt, sin, cos, atan2, pi



class Link:
    def __init__(self, pos, size, angle, type):
        self.pos = Vector2(pos)
        self.size = size
        self.angle = 0

        self.vel = Vector2(0, 0)

        self.deceleration = Vector2(0.06, 0.06)

        self.col = '#808080'
        self.col2 = '#909000'

        self.left_link = None
        self.right_link = None

        self.type = type

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

    def move(self):
        self.pos += self.vel

    def decelerate(self):
        self.vel -= self.deceleration

        self.vel[0] = max(0, self.vel[0])
        self.vel[1] = max(0, self.vel[1])

    def update_direction(self):
        x3, y3 = get_average_point(self.left_link.pos, self.right_link.pos)

        self.angle = get_angle(self.pos, (x3, y3))

        #self.direction = Vector2(cos(self.angle), sin(self.angle))

    def update_deceleration(self):
        x, y = get_average_point(self.left_link.pos, self.right_link.pos)

        dist = get_dist(self.pos, (x,y))

        self.deceleration = 0

    def attract_right(self):
        if self.type in ['body', 'head']:
            A = self.right_link.pos
            B = self.pos
            rad = self.size[0]

            force = get_force(A, B, rad)

            self.right_link.pos += force

    def apply_force(self):
        if self.type == 'body':
            A = self.pos
            B = get_average_point(self.left_link.pos, self.right_link.pos)
            rad = self.size[0]

            force = get_force(A, B, rad)

            self.vel += force


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

def get_average_point(A, B):
    x1, y1 = A
    y2, x2 = B

    return (x1 + x2) / 2, (y1 + y2) /2

def get_force(A, B, rad):
    dist = get_dist(A, B)
    angle = get_angle(A, B)

    force_x = cos(angle) * (dist - rad) / sett.FORCE_FACTOR
    force_y = sin(angle) * (dist - rad) / sett.FORCE_FACTOR

    force_x = min(1, force_x)
    force_y = min(1, force_y)

    return Vector2(force_x, force_y)


def update_all(links):
    for link in links:
        link.apply_force()
        link.move()

        link.attract_right()


def create_body(n):
    body = []

    head_pos = 500, 80
    w, h = 30, 30
    type = 'body'

    for i in range(n):
        x = head_pos[0]
        y = head_pos[1] + w

        new_link = Link((x,y), (w,h), 0, type)

        body.append(new_link)

    for i, link in enumerate(body[1:-1]):
        link.left_link = body[i - 1]
        link.right_link = body[i + 1]

    body[0].type = 'head'
    body[-1].type = 'tail'

    return body








