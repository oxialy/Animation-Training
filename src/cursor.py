

import pygame


class Cursor:
    def __init__(self, pos, colors, n, interval, min_max):
        self.bar_pos = pos
        self.h = 11

        self.col = colors[0]
        self.col2 = colors[1]

        self.number_of_graduations = n
        self.interval_size = interval
        self.length = n * interval

        self.cursor_pos = 0

        self.val = 0
        self.min = min_max[0]
        self.max = min_max[1]

    def draw(self, win):
        self.draw_bar(win)
        self.draw_graduation(win)
        self.draw_cursor(win)

    def draw_bar(self, win):
        x, y = self.bar_pos

        A = x, y + self.h / 2
        B = x + self.length, y + self.h / 2

        pygame.draw.line(win, self.col, A, B, 2)

    def draw_graduation(self, win):
        for i in range(self.number_of_graduations):
            pos_x = i * self.interval_size
            pos_y = 0

            A = pos_x, pos_y
            B = pos_x, pos_y + self.h

            pygame.draw.line(win, self.col, A, B, 1)

    def draw_cursor(self, win):
        x, y = self.cursor_pos, 0

        A = x, y
        B = x, y + self.h

        pygame.draw.line(win, self.col2, A, B, 3)

    def update_pos(self, val):
        value_interval = (self.max - self.min) / self.number_of_graduations

        x = round(self.interval_size * (val - self.min) / value_interval)

        self.cursor_pos = x
