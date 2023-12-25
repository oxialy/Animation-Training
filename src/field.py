from src import drawing_variables as dv
from src import msc

from src.drawing_variables import colors


import pygame

from pygame import Vector2



class Field:
    def __init__(self):
        self.pos = 0

        self.field = []

        self.up_wall = None
        self.down_wall = None
        self.left_wall = None
        self.right_wall = None
        self.wall = [self.up_wall, self.down_wall, self.right_wall, self.left_wall]

    def draw(self, win):
        for wind in self.field:
            wind.draw(win)

    def move_all(self, boundaries):
        for wind in self.field:
            wind.move()
            if wind.check_wall(boundaries):
                wind.tp()

    def apply_force_all(self):
        for wind in self.field:
            wind.apply_force()


class Wind:
    def __init__(self, pos, rad, col, vel, force):
        self.pos = Vector2(pos)
        self.rad = rad

        self.vel = vel
        self.vel2 = Vector2(2, 0)

        self.force = Vector2(force)
        self.col = col

        self.active = True

        self.active_attr = {
            'col': col,
            'vel': vel
        }
        self.inactive_attr = {
            'col': colors['blue2'],
            'vel': Vector2(2, 0)
        }


    def __repr__(self):
        return repr(self.force)


    def draw(self, win):
        pygame.draw.circle(win, self.col, self.pos, self.rad, 1)


    def move(self):
        self.pos += self.vel

    def tp(self):
        self.pos[0] = 10

    def check_wall(self, boundaries):
        x,y = self.pos
        w,h = self.rad * 2, self.rad * 2

        rect = msc.centered_rect((x,y,w,h))

        for bound in boundaries:
            if rect.colliderect(bound):
                return True

    def apply_force(self, link):
        if link.type in ['body', 'tail'] and self.active:
            link.vel += self.force

    def check_apply_force(self, links):
        pass

    def activate(self):
        self.col = self.active_attr['col']
        self.vel = self.active_attr['vel']

    def deactivate(self):
        self.col = self.inactive_attr['col']
        self.vel = self.inactive_attr['vel']



















