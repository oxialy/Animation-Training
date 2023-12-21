import random

from src import game_functions as GF
from src import settings as sett


from .settings import WIDTH, HEIGHT


import pygame, random
from random import randrange


def create_parts(n):
    parts = []
    for i in range(n):
        x = randrange(0, 500)
        y = randrange(0, 500)
        w,h = 30, 30

        new_part = GF.Part((x,y),(w,h))

        parts.append(new_part)

    return parts


def get_color_range(k_r=1, k_g=5, k_b=1/80):
    colA = []

    r_range = range(40,241)
    g_range = range(40,241)
    b_range = range(40,241)

    for r,g,b in zip(r_range, g_range, b_range):
        colA.append((r//k_r, g//k_g, 1//k_b))

    return colA


#tile1 = GF.Tile((4,4), (200, 30))

colA = get_color_range()
colB = get_color_range(10, 3, 2)

animated_tiles = []


nearest_parts = create_parts(7)

pos = 0,0

selection = None

DRAWLINE = False


questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]





