import pygame as pg
from pygame.locals import *

from game_state_handler.gamestate import GameState


class MainMenu(GameState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.next_state = "GAMEPLAY"

    def startup(self, persistent: dict):
        self.persist = persistent

        pg.display.set_caption("2D game - Menu")

        self.done = True

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True

    def update(self, dt: int):
        pass

    def draw(self):
        pass
