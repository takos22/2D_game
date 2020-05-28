import pygame as pg
from pygame.locals import *


class Game(object):
    """
    A single instance of this class is responsible for
    managing which individual game state is active
    and keeping it updated. It also handles many of
    pygame's nuts and bolts (managing the event
    queue, framerate, updating the display, etc.).
    and its run method serves as the "game loop".
    """

    def __init__(self, states: dict, start_state: str):
        """
        Initialize the Game object.

        screen: the pygame display surface
        states: a dict mapping state-names to Game_state objects
        start_state: name of the first active game state
        """
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 32
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]
        self.persistent = {}

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pg.event.get():
            self.state.get_event(event)

    def startup(self):
        """Start up the first state"""
        self.state.startup(self.persistent)

    def flip_state(self):
        """Switch to the next game state."""
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        self.persistent.update(self.state.persist)
        self.state = self.states[self.state_name]
        self.state.startup(self.persistent)

    def update(self, dt):
        """
        Check for state flip and update active state.

        dt: milliseconds since last frame
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw()

    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        self.startup()
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
