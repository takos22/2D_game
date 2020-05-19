import pygame as pg
from pygame.locals import *

from game_state_handler.gamestate import GameState
from menu_elements.MenuElements import Menu


class MainMenu(GameState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.next_state = "GAMEPLAY"

    def startup(self, persistent: dict):
        self.persist = persistent

        self.size = self.width, self.height = (800, 800)

        self.screen = pg.display.set_mode(self.size)
        pg.display.set_caption("2D game - Menu")

        self.menu = Menu(self.screen, pg.Color("black"), "arial")
        self.menu.add_text("title", (self.width/2, self.height/2), "2D game", 72)

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True
        elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            self.done = True

    def update(self, dt: int):
        pass

    def draw(self):
        self.screen.fill(pg.Color("white"))
        self.menu.draw()
        pg.display.flip()
