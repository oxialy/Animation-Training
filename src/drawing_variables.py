from src import settings as sett
from src.cursor import Cursor

from .settings import WIDTH, HEIGHT

import pygame



colors = {
    'blue1': '#102080',
    'blue2': '#1828A0',
    'lightblue1': '#4040B3',
    'darkblue1': '#08263c',
    'seagreen1': '#106040',
    'orange1': '#806020',
    'lightgrey1': '#aaaaaa',
    'darkgrey1': '#404040',
    'grey1': '#707070',
    'red1': '#A01010',
    'purple1': '#901080',
    'lightpurple1': '#aa70aa',
    'cyan1': '#018090',
    'green1': '#017028',
    'green2': '#186540'
}

bg_color = '#011320'

#bg_color = '#010111'


bar_1_pos = 100, 30
bar_1 = pygame.Surface((250, 25))
bar_1_bg_color = bg_color

col1 = (colors['grey1'], colors['orange1'])
gravity_cursor = Cursor((0,0), col1, 60, 7, (-0.3, 0.3))




