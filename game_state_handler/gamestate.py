import pygame as pg
from pygame.locals import *


class GameState(object):
    """
    Parent class for individual game states to inherit from.
    """

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.persist = {}
        self.font = pg.font.Font(None, 24)

    def startup(self, persistent: dict):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent

    def get_event(self, event: pg.event.Event):
        """
        Handle a single event passed by the Game object.
        """
        pass

    def update(self, dt: int):
        """
        Update the state. Called by the Game object once
        per frame.

        dt: time since last frame
        """
        pass

    def draw(self):
        """
        Draw everything to the screen.
        """
        pass
