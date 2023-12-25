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



class Link:
    def __init__(self, pos, size, angle, type, i):
        self.pos = Vector2(pos)
        self.size = size
        self.angle = 0

        self.vel = Vector2(0, 0)

        self.deceleration = 0.94
        self.max_vel = 2

        self.col = colors['seagreen1']
        self.col2 = '#909000'

        self.left_link = None
        self.right_link = None

        self.type = type
        self.i = i

        self.distance_from_mouse = 0
        self.selected = False

        self.count = 0

    def __repr__(self):
        return repr((self.i, self.type, self.vel))

    def draw(self, win):
        w, h = self.size

        x = self.pos[0] - w // 2
        y = self.pos[1] - h // 2


        pygame.draw.ellipse(win, self.col, (x,y,w,h), 8)
        #pygame.draw.ellipse(win, self.col2, (self.pos, (2,2)))

        self.draw_inner(win)

        if self.selected:
            pygame.draw.ellipse(win, colors['cyan1'], (x,y,w,h), 0)

            if self.left_link and self.right_link:
                x, y = get_average_point(self.left_link.pos, self.right_link.pos)
                w, h = 6,6

                rect = msc.centered_rect((x,y,w,h))

                pygame.draw.ellipse(win, colors['red1'], rect)

    def draw_inner(self, win):
        x,y = self.pos
        w,h = self.size[0] // 2, self.size[1] // 2
        w,h = 4, 4

        rect = msc.centered_rect((x,y,w,h))
        pygame.draw.ellipse(win, self.col2, rect)

    def draw_left(self, win):
        x,y = self.left_link.pos
        w,h = 5, 5

        rect = msc.centered_rect((x,y,w,h))
        pygame.draw.ellipse(win, colors['orange1'], rect)

    def draw_right(self, win):
        x,y = self.right_link.pos
        w,h = 5, 5

        rect = msc.centered_rect((x,y,w,h))
        pygame.draw.ellipse(win, colors['orange1'], rect)


    def draw_line(self, win, pos):
        pygame.draw.line(win, self.col2, self.pos, pos)

    def move(self):
        self.pos += self.vel

    def decelerate(self):
        self.vel *= self.deceleration

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

            force = get_force(A, B, rad, 80)

            self.right_link.pos += force

    def apply_force(self):
        if self.type in ['body', 'tail']:
            A = self.pos

            if self.type == 'body':
                B = get_average_point(self.left_link.pos, self.right_link.pos)
                rad = 0
                force_factor = 10
            elif self.type == 'tail':
                B = self.left_link.pos
                rad = self.size[0]
                force_factor = 40

            force = get_force(A, B, rad, force_factor)

            self.vel += force

            self.count += 1

            if self.count < 3:
                print(self.count, force, self)

    def cap_velocity(self):
        x, y = self.vel

        vel_norm = sqrt((x ** 2 + y ** 2))

        if vel_norm > self.max_vel:
            k = self.max_vel / vel_norm
            self.vel *= k

    def is_clicked(self, pos):
        x, y = self.pos
        w, h = self.size

        rect = msc.centered_rect((x,y,w,h))

        if rect.collidepoint(pos):
            return True

    def is_on_wind(self, fields):
        x, y = self.pos
        w, h = self.size

        rect = msc.centered_rect((x,y,w,h))

        for field in fields:
            for wind in field.field:
                x, y = wind.pos
                w, h = wind.rad * 2, wind.rad * 2
                wind_rect = msc.centered_rect((x,y,w,h))
                if rect.colliderect(wind_rect):
                    return wind


    def update_color(self, colA, colB):
        color_index = int(self.distance_from_mouse * 200 / 500)
        color_index = min(200, color_index)

        self.col = colA[color_index]
        self.col2 = colB[color_index]

    def update_distance(self, pos):
        self.distance_from_mouse = get_dist(self.pos, pos)



class Cursor:
    def __init__(self):
        self.start = Vector2(0, 0)
        self.end = Vector2(0, 0)

        self.len = 0
        self.force = Vector2(0, 0)

        self.color = colors['purple1']
        self.col2 = colors['lightblue1']

    def draw(self, win):
        pygame.draw.line(win, self.color, self.start, self.end)
        pygame.draw.circle(win, self.col2, self.start, 4, 1)
        pygame.draw.circle(win, self.col2, self.end, 3)


    def set_force(self):
        self.force = get_force(self.start, self.end, 0, 200)

    def set_pos(self, pos):
        self.start = pos
        self.end = pos


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


def get_force(A, B, rad, force_factor=30):
    dist = get_dist(A, B)
    angle = get_angle(A, B)

    force_x = cos(angle) * (dist - rad) / force_factor
    force_y = sin(angle) * (dist - rad) / force_factor

    force_x = min(1.5, force_x)
    force_y = min(1.7, force_y)

    return Vector2(force_x, force_y)


def update_all(links, fields=()):
    for link in links:
        link.apply_force()
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

def update_fields(fields, boundaries):
    for field in fields:
        field.move_all(boundaries)

def toggle_field(winds):
    for wind in winds:
        wind.active = not wind.active
        if wind.active:
            wind.activate()
        else:
            wind.deactivate()

def cap_velocity_all(links):
    for link in links:
        link.cap_velocity()


def check_selected(links, pos):
    for link in links:
        if link.is_clicked(pos):
            link.selected = True
            return link

def create_body(n, pos=(500,80), size=15):
    body = []

    head_pos = pos
    w, h = size, size
    type = 'body'

    for i in range(n):
        x = head_pos[0]
        y = head_pos[1] + i * w
        if i == 0:
            type = 'head'
        elif i == n - 1:
            type = 'tail'
        else:
            type = 'body'

        new_link = Link((x,y), (w,h), 0, type, i)

        print(new_link)
        body.append(new_link)

    for link in body[1:]:
        link.left_link = body[link.i - 1]

    for link in body[:-1]:
        link.right_link = body[link.i + 1]

    body[0].type = 'head'
    body[-1].type = 'tail'

    return body


def create_field(n):
    field = Field()

    COL_SIZE = (sett.WIDTH - 40) // n
    ROW_SIZE = 10

    min_norm, max_norm = 0, 10
    k = 205 // max_norm

    y = randrange(100, 700)
    force = Vector2(0, 0)
    angle = 0
    norm = randrange(min_norm, max_norm)

    increment = -1

    for i in range(n):
        x = 20 + COL_SIZE * i
        y += choice([-1, 1]) * ROW_SIZE

        vel = Vector2(7, 0)

        norm += increment
        norm = max(min_norm, min(max_norm, norm))

        force = Vector2(get_point_from_angle((0,0), angle, norm)) / 20

        r, g, b = 100 - norm * k * 0.5, norm * k * 0.8, norm * k * 0.5 + 60
        r, g, b = max(0, min(250, r)), max(0, min(250, g)), max(0, min(250, b))

        if not min_norm < norm < max_norm:
            increment *= -1

        wind = Wind((x,y), 8, (r,g,b), vel, force)
        wind.col = r,g,b

        field.field.append(wind)

    print(field.field[0])
    return field













