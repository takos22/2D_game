import pygame as pg
from pygame.locals import *


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.pos = pg.Vector2(x, y)
        self.vel = pg.Vector2(0, 0)
        self.size = pg.Vector2(8, 8)
        self.max_vel = 50  # px/sec

        self.rect = pg.Rect(self.pos.x + 4, self.pos.y + 4,
                            self.size.x, self.size.y)
        self.update_rect = pg.Rect(self.pos.x - 16 if self.pos.x >= 16 else 0,
                                   self.pos.y - 16 if self.pos.y >= 16 else 0,
                                   16*5, 16*5)

        self.animation_i = 0
        self.last_animation = "[0, -1]"
        self.animations = {
            direction[0]: [pg.image.load(f"assets\\animation\\player\\walk_{direction[1]}_{i}.png")
                           for i in range(4)]
            for direction in [("[0, -1]", "up"), ("[0, 1]", "down"), ("[-1, 0]", "left"), ("[1, 0]", "right")]
        }

    def move(self, dt, collideable):
        temp = pg.Vector2(self.pos + self.vel*(self.max_vel*(dt/1000)))
        self.rect.topleft = (temp.x+4, temp.y+4)

        if pg.sprite.spritecollideany(self, collideable):
            if self.vel.x:
                self.collision(dt, collideable, 0)
            if self.vel.y:
                self.collision(dt, collideable, 1)

        else:
            self.pos = pg.Vector2(temp)

            self.update_rect.center = self.rect.center
            self.update_rect.topleft = (self.update_rect.left if self.update_rect.left >= 0 else 0,
                                        self.update_rect.top if self.update_rect.top >= 0 else 0)
            self.update_rect.bottomright = (self.update_rect.right if self.update_rect.right <= 640 else 640,
                                            self.update_rect.bottom if self.update_rect.bottom <= 640 else 640)

    def collision(self, dt, collideable, i):
        if i:
            pos = self.pos.y
            vel = self.vel.y
        else:
            pos = self.pos.x
            vel = self.vel.x

        pos += vel*(self.max_vel*(dt/1000))
        self.rect[i] = pos
        collision = pg.sprite.spritecollideany(self, collideable)
        while collision:
            if self.rect[i] < collision.rect[i]:
                self.rect[i] = collision.rect[i]-self.rect.size[i]
            else:
                self.rect[i] = collision.rect[i]+collision.rect.size[i]
            collision = pg.sprite.spritecollideany(self, collideable)

    def draw(self, screen: pg.Surface):
        self.draw_rect = pg.Rect(self.rect.x - 4, self.rect.y - 20, 16, 32)
        if tuple(self.vel) == (0.0, 0.0):
            screen.blit(
                self.animations[self.last_animation][0], self.draw_rect)
        else:
            self.last_animation = str(self.vel) if str(self.vel) in [
                "[0, -1]", "[0, 1]", "[-1, 0]", "[1, 0]"] else f"[{int(self.vel.x)}, 0]"
            screen.blit(self.animations[self.last_animation]
                        [self.animation_i//5], self.draw_rect)
            self.animation_i += 1
            if self.animation_i >= 20:
                self.animation_i = 0
