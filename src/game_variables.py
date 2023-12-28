import random

from src import game_functions as GF
from src import settings as sett


from .settings import WIDTH, HEIGHT


import pygame, random
from random import randrange


def create_links(n):
    links = []
    for i in range(n):
        x = randrange(0, 500)
        y = randrange(0, 500)
        w,h = 30, 30
        angle = 0
        type = 'body'

        new_link = GF.Link((x,y),(w,h), angle, type, i)

        links.append(new_link)

    return links

def unpack_bodies(bodies):
    links = []
    for body in bodies:
        for link in body:
            links.append(link)
    return links

def unpack_fields(fields):
    winds = []
    for field in fields:
        for wind in field.field:
            winds.append(wind)
    return winds


def get_color_range(k_r=1, k_g=5, k_b=1/80):
    colA = []

    r_range = range(40,241)
    g_range = range(40,241)
    b_range = range(40,241)

    for r,g,b in zip(r_range, g_range, b_range):
        colA.append((r//k_r, g//k_g, 1//k_b))

    return colA

def dim_color(fields):
    k = 1
    for field in fields:
        for wind in field.field:
            r, g, b = wind.col
            wind.col = r / k, g / k, b / k


#tile1 = GF.Tile((4,4), (200, 30))

colA = get_color_range(1.8, 4, 1/110)
colB = get_color_range(10, 3, 2)


GRAVITY_INTENSITY = 0.02

animated_tiles = []

nearest_links = create_links(7)

all_links = []
all_winds = []

body = GF.create_body(sett.BODY_LENGTH, (500, 470), 5)

grass_field = GF.create_bodies(10)

all_links = unpack_bodies(grass_field + [body])

cursor = GF.Cursor()


FIELD_LENGTH = 70

field = GF.create_field(FIELD_LENGTH)
f1 = GF.create_field(FIELD_LENGTH)
f2 = GF.create_field(FIELD_LENGTH)
f3 = GF.create_field(FIELD_LENGTH)
f4 = GF.create_field(FIELD_LENGTH)
f5 = GF.create_field(FIELD_LENGTH)
f6 = GF.create_field(FIELD_LENGTH)
f7 = GF.create_field(FIELD_LENGTH)
f8 = GF.create_field(FIELD_LENGTH)
f9 = GF.create_field(FIELD_LENGTH)
f10 = GF.create_field(FIELD_LENGTH)

fields = [f1, f2, f3, field]
all_winds = unpack_fields(fields)


dim_color(fields)

pos = 0,0

LEFT_BOUNDARY = pygame.Rect((-10, 0, 10, HEIGHT))
RIGHT_BOUNDARY = pygame.Rect((WIDTH + 10, 0, 10, HEIGHT))

WALLS = LEFT_BOUNDARY, RIGHT_BOUNDARY


selection = None

DRAWLINE = False
TOGGLE_FIELD = True


questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]






