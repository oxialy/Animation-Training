import random

from src import game_functions as GF
from src import settings as sett


from .settings import WIDTH, HEIGHT


import pygame, random
from random import randrange


def create_body_part(n):
    bodyparts = []
    for i in range(n):
        x = randrange(0, 500)
        y = randrange(0, 500)
        w,h = 30, 30

        new_bodypart = GF.BodyPart((x,y),(w,h))

    bodyparts.append(new_bodypart)



colA = [(r,g,b) for r,g,b in zip(range(0))]

def get_color_range():

    colA = []

    r_range = range(40,240)
    g_range = range(40,240)
    b_range = range(40,240)

    for r,g,b in zip(r_range, g_range, b_range):
        colA.append((r, g//5, 80))

    return colA


#tile1 = GF.Tile((4,4), (200, 30))

animated_tiles = []


nearest_parts = create_body_part(7)

pos = 0,0

questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]






