from src import settings as sett
from src import drawing_variables
from src import game_functions
from src import msc

from src.drawing_variables import colors
from src.game_functions import get_dist, get_force, get_angle, get_point_from_angle, get_average_point



import pygame, math, random

from pygame import Vector2
from math import pi, sqrt
from random import randrange



class Link:
    def __init__(self, pos, size, angle, type, i):
        self.pos = Vector2(pos)
        self.size = size
        self.angle = pi/2

        self.vel = Vector2(0, 0)

        self.deceleration = 0.90
        self.max_vel = 2

        self.col = colors['green2']
        self.col2 = '#60a0b0'

        self.left_link = None
        self.right_link = None

        self.type = type
        self.i = i

        self.distance_from_mouse = 0
        self.SELECTED = False
        self.TOGGLE_ANGLE = True

        self.count = 0

    def __repr__(self):
        return repr((self.i, self.type, self.vel))

    def draw(self, win):
        w, h = self.size

        x = self.pos[0] - w // 2
        y = self.pos[1] - h // 2

        #pygame.draw.ellipse(win, self.col2, (x,y,w,h))

        pygame.draw.ellipse(win, self.col, (x,y,w,h), 0)

        self.draw_inner(win)

        if self.SELECTED:
            pygame.draw.ellipse(win, colors['cyan1'], (x,y,w,h), 0)

            if self.left_link and self.right_link:
                x, y = get_average_point(self.left_link.pos, self.right_link.pos)
                w, h = 6,6

                rect = msc.centered_rect((x,y,w,h))

                pygame.draw.ellipse(win, colors['red1'], rect)

        if self.TOGGLE_ANGLE:
            self.draw_angle(win)

    def draw_angle(self, win):
        A = self.pos
        B = get_point_from_angle(self.pos, self.angle, self.size[0])

        pygame.draw.line(win, 'grey', A, B)

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

        if self.type == 'body':
            self.angle = get_angle(self.left_link.pos, self.pos)
        elif self.type == 'head' and False:
            self.angle = get_angle(self.pos, self.right_link.pos)
        elif self.type == 'tail':
            self.angle = get_angle(self.left_link.pos, self.pos)

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
        if self.type in ['body']:
            A = self.pos

            if self.type == 'body':
                B = get_average_point(self.left_link.pos, self.right_link.pos)
                rad = 0
                force_factor = self.size[0] * 2
            elif self.type == 'tail':
                B = self.left_link.pos
                rad = self.size[0]
                force_factor = 40

            force = get_force(A, B, rad, force_factor)

            self.vel += force

            self.count += 1

            if self.count < 3:
                print(self.count, force, self)

    def apply_angular_force(self):
        if self.type in ['tail', 'body']:
            A = self.pos
            B = get_point_from_angle(self.left_link.pos, self.left_link.angle, self.size[0])
            rad = 0
            force_factor = self.size[0] * 6

            force = get_force(A, B, rad, force_factor)

            self.vel += force

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




def toggle_angle(links):
    for link in links:
        link.TOGGLE_ANGLE = not link.TOGGLE_ANGLE

def cap_velocity_all(links):
    for link in links:
        link.cap_velocity()


def check_selected(links, pos):
    for link in links:
        if link.is_clicked(pos):
            link.SELECTED = True
            return link

def create_body(n, pos=(500,80), size=15):
    body = []

    head_pos = randrange(20, sett.WIDTH - 20), randrange(80, 120) + 400
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

def create_bodies(n, length, size=10):
    all_bodies = []

    for i in range(n):
        l = randrange(length, length + 6)
        new_body = create_body(l, size=size)

        all_bodies.append(new_body)

    return all_bodies










