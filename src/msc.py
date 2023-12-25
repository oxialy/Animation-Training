import pygame


def centered_rect(rect):
    x,y,w,h = rect

    x2 = x - w // 2
    y2 = y - h // 2

    return pygame.Rect(x2,y2, w,h)


def get_highest_wind(field):
    f2 = sorted(field, key=lambda wind: wind.force[0])

    return f2[0]











