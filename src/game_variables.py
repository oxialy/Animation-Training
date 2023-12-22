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

        new_link = GF.Link((x,y),(w,h), angle, type)

        links.append(new_link)

    return links


def get_color_range(k_r=1, k_g=5, k_b=1/80):
    colA = []

    r_range = range(40,241)
    g_range = range(40,241)
    b_range = range(40,241)

    for r,g,b in zip(r_range, g_range, b_range):
        colA.append((r//k_r, g//k_g, 1//k_b))

    return colA


#tile1 = GF.Tile((4,4), (200, 30))

colA = get_color_range(1.6)
colB = get_color_range(10, 3, 2)

animated_tiles = []


nearest_links = create_links(7)

body = GF.create_body(10)

pos = 0,0

selection = None

DRAWLINE = False


questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]






