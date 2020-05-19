import pygame as pg
from pygame.locals import *

from game_elements.collideable import Collideable


class Wall(Collideable):
    def __init__(self, x, y, w, h):
        super(Wall, self).__init__(x, y, w, h)

    def draw(self, screen: pg.Surface):
        super(Wall, self).draw(screen)
        pg.draw.rect(screen, pg.Color("black"), self.rect)
