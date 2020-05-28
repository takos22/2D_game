import pygame as pg


class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Tile, self).__init__()
        self.pos = pg.Vector2(x, y)
        self.image = image

        self.rect = pg.Rect(self.pos.x, self.pos.y, 16, 16)
