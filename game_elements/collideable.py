import pygame as pg
from pygame.locals import *


class Collideable():
    def __init__(self, x, y, w, h):
        self.pos = pg.Vector2(x, y)
        self.size = pg.Vector2(w, h)

        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

    def draw(self, screen: pg.Surface):
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
