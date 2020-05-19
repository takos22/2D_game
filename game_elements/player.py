import pygame as pg
from pygame.locals import *


class Player():
    def __init__(self, x, y):
        self.pos = pg.Vector2(x, y)
        self.vel = pg.Vector2(0, 0)
        self.size = pg.Vector2(32, 32)

        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

    def move(self, walls):
        self.pos += self.vel
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

        if self.rect.collidelistall(walls):
            self.pos -= self.vel
            self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, pg.Color("red"), self.rect)
