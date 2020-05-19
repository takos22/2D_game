import pygame as pg
from pygame.locals import *

from game_state_handler.gamestate import GameState


class Gameplay(GameState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "MAINMENU"

    def startup(self, persistent: dict):
        self.persist = persistent

        pg.display.set_caption("2D game")

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True

    def update(self, dt: int):
        pass

    def draw(self):
        pass
