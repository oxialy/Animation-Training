from src import drawing_variables as dv
from src import settings as sett
from src import msc

from .drawing_variables import colors
from src.field import Field, Wind

import pygame
import math
import random

from pygame import Vector2
from math import sqrt, sin, cos, atan2, pi
from random import randrange, choice


class Cursor:
    def __init__(self):
        self.start = Vector2(0, 0)
        self.end = Vector2(0, 0)

        self.color = colors['purple1']
        self.col2 = colors['lightblue1']

        self.len = 0
        self.force = Vector2(0, 0)

        self.max_norm = 1.4

    def draw(self, win):
        pygame.draw.line(win, self.color, self.start, self.end)
        pygame.draw.circle(win, self.col2, self.start, 4, 1)
        pygame.draw.circle(win, self.col2, self.end, 3)


    def set_force(self):
        self.force = get_force(self.start, self.end, 0, 200)

        x, y = self.force

        norm = sqrt(x ** 2 + y ** 2)

        if norm != 0:
            k = self.max_norm / norm

            if norm > self.max_norm:
                self.force *= k
                self.color = colors['red1']
            else:
                self.color = colors['purple1']

    def set_pos(self, pos):
        self.start = pos
        self.end = pos

    def shorten(self):
        force = get_force(self.end, self.start, 0, 60, 50)
        self.end += force


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

    x2 = x1 + cos(angle) * dist
    y2 = y1 + sin(angle) * dist

    return x2, y2


def get_average_point(A, B):
    x1, y1 = A
    x2, y2 = B

    return (x1 + x2) / 2, (y1 + y2) /2


def get_tail_resting_pos(body):
    tail = body[-1]
    left_link = tail.left_link
    rad = tail.size[0]

    force = get_force(tail.pos, left_link.pos, rad)


def get_force(A, B, rad, force_factor=30, min_force=0):
    dist = get_dist(A, B)
    angle = get_angle(A, B)

    force_x = cos(angle) * (dist - rad + min_force) / force_factor
    force_y = sin(angle) * (dist - rad + min_force) / force_factor

    force_x = min(1.5, force_x)
    force_y = min(1.7, force_y)

    return Vector2(force_x, force_y)


def apply_gravity(link, intensity):
    if link.type in ['body', 'tail']:
        link.vel += Vector2(0, intensity)


def update_all(links, fields=(), gravity_intensity=0.02):
    for link in links:
        link.apply_force()
        link.apply_angular_force()
        apply_gravity(link, gravity_intensity)
        link.move()

        #link.attract_right()
        link.decelerate()

        current_wind = link.is_on_wind(fields)

        if current_wind:
            current_wind.apply_force(link)

        link.cap_velocity()


def update_all_bodies(bodies, fields=()):
    for body in bodies:
        update_all(body, fields)


def create_field(n):
    field = Field()

    COL_SIZE = (sett.WIDTH - 40) // n
    ROW_SIZE = 10

    min_norm, max_norm = 0, 10
    k = 205 // max_norm

    y = randrange(320, 580)
    vel = Vector2(4, 0)
    force = Vector2(0, 0)
    angle = 0
    norm = sqrt(randrange(min_norm, max_norm))

    increment = -0.3 * choice([-1, 1])

    for i in range(n):
        x = 20 + COL_SIZE * i
        y += choice([-1, 1]) * ROW_SIZE

        norm += increment
        norm2 = norm ** 2
        norm2 = max(min_norm, min(max_norm, norm2))

        force = Vector2(get_point_from_angle((0,0), angle, norm2)) / 120

        r, g, b = 100 - norm2 * k * 0.5, norm2 * k * 0.8, norm2 * k * 0.5 + 60
        r, g, b = max(0, min(250, r)), max(0, min(250, g)), max(0, min(250, b))

        if not min_norm < norm2 < max_norm:
            increment *= -1

        wind = Wind((x,y), 6, (r,g,b), vel, force)
        wind.col = r,g,b

        field.field.append(wind)

    print(field.field[0])
    return field













