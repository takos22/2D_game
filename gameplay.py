import json
import pygame as pg
from pygame.locals import *

from game_state_handler.gamestate import GameState
from game_elements.player import Player
from game_elements.wall import Wall


class Gameplay(GameState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "MAINMENU"

    def startup(self, persistent: dict):
        self.persist = persistent

        self.player = Player(64, 64)
        self.game_state = "start"
        with open("maps.json") as f:
            self.maps = json.loads(f.read())
        self.walls = [Wall(*coords) for coords in self.maps[self.game_state]]
        self.max_vel = 4

        self.size = self.width, self.height = (800, 800)

        self.screen = pg.display.set_mode(self.size)
        pg.display.set_caption("2D game")

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
                self.player.vel.y = self.max_vel
            elif event.key == K_UP:
                self.player.vel.y = -self.max_vel
            elif event.key == K_RIGHT:
                self.player.vel.x = self.max_vel
            elif event.key == K_LEFT:
                self.player.vel.x = -self.max_vel

    def update(self, dt: int):
        self.player.move(self.walls)

    def draw(self):
        self.screen.fill(pg.Color("white"))
        for wall in self.walls:
            wall.draw(self.screen)
        self.player.draw(self.screen)

        pg.display.flip()
