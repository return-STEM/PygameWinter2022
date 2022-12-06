import pygame
from pygame.locals import *
import sys
import random
import time
from pygame.math import Vector2

SCREEN_W = 640
SCREEN_H = 480
FRAMES_PER_SECOND = 30

# Setting up Pygame
# ----------------------------------------------------------------------------------------------------------------------
pygame.init()
frame_clock = pygame.time.Clock()
display = pygame.display.set_mode((SCREEN_W, SCREEN_H))  # Ordered pair (tuple) of screen width and height
pygame.display.set_caption("My Game")


# ----------------------------------------------------------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Code specific to a Player that will run ONCE on setup
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------

    def update(self):
        # Code specific to a Player that will run every frame
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------
        pass

    def on_key_down(self, key_event):
        # Code specific to a Player that will run whenever a key is pressed.
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------
        pass

    def late_update(self):
        # Code specific to a Player that will run every frame AFTER update() and on_key_down()
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------
        pass


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Code specific to a Platform that will run ONCE on setup
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------

    def update(self):
        # Code specific to a Platform that will run every frame
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------
        pass


def main():
    # Initialization code - runs only when we start the game
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # Event loop - runs every frame
    # ------------------------------------------------------------------------------------------------------------------
    while True:
        # Code that runs every frame

        # Cycle through all the events (user inputs)
        for event in pygame.event.get():
            # If the event is a quit (X out of the window)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        frame_clock.tick(FRAMES_PER_SECOND)
    # ------------------------------------------------------------------------------------------------------------------


# Run the main() function. Ignore this - just edit main()
main()
