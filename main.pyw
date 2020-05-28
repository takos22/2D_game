import pygame as pg

from game_state_handler.game import Game
from gameplay import Gameplay
from mainmenu import MainMenu

if __name__ == "__main__":
    pg.init()
    states = {
        "MAINMENU": MainMenu(),
        "GAMEPLAY": Gameplay()
    }
    game = Game(states, "MAINMENU")
    game.run()
    pg.quit()
