import json
import pygame as pg
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame

from game_state_handler.gamestate import GameState
from game_elements.player import Player
from game_elements.tile import Tile


class Gameplay(GameState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "GAMEPLAY"

    def startup(self, persistent: dict):
        self.persist = persistent
        self.persist["game_state"] = "start"
        self.game_state = self.persist["game_state"]

        self.player = Player(17*16, 10*16)

        self.size = self.width, self.height = (640, 640)

        self.screen = pg.display.set_mode(self.size)
        pg.display.set_caption("2D game")

        self.map = load_pygame(f"assets\\maps\\{self.game_state}.tmx", pixelalpha=True)
        self.layers = {
            layer.name.lower(): layer for layer in self.map.visible_layers}
        self.collideable = pg.sprite.Group([Tile(x*16, y*16, image) for x, y, image in
                                            list(self.layers["collideable terrain"].tiles()) + list(self.layers["collideable"].tiles())])

        for i, layer in enumerate(self.map.visible_layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                for x in range(0, self.width//16):
                    for y in range(0, self.height//16):
                        image = self.map.get_tile_image(x, y, i)
                        if image != None:
                            self.screen.blit(image, (16*x, 16*y))
        pg.display.flip()

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True

        elif event.type == KEYUP:
            if event.key == K_DOWN:
                self.player.vel.y = 0
            elif event.key == K_UP:
                self.player.vel.y = 0
            elif event.key == K_RIGHT:
                self.player.vel.x = 0
            elif event.key == K_LEFT:
                self.player.vel.x = 0

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.player.vel.y = 1
            elif event.key == K_UP:
                self.player.vel.y = -1
            elif event.key == K_RIGHT:
                self.player.vel.x = 1
            elif event.key == K_LEFT:
                self.player.vel.x = -1

    def update(self, dt):
        self.player.move(dt, self.collideable)

    def draw(self):
        for i, layer in enumerate(self.map.visible_layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                if layer.name.lower() == "player":
                    self.player.draw(self.screen)

                else:
                    for x in range(self.player.update_rect.left//16, self.player.update_rect.right//16):
                        for y in range(self.player.update_rect.top//16, self.player.update_rect.bottom//16):
                            image = self.map.get_tile_image(x, y, i)
                            if image != None:
                                self.screen.blit(image, (16*x, 16*y))

        pg.display.update([self.player.update_rect])
