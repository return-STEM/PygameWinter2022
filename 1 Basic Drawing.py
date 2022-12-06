import pygame
from pygame.locals import *
import sys
import random
import time
from pygame.math import Vector2
from pygame.color import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

SCREEN_W = 640
SCREEN_H = 480
FRAMES_PER_SECOND = 30

# LESSON PLAN
# Create the platform first, and draw it on the screen
# Create the player, and draw it on the screen
# Move on to the next file


# Setting up Pygame
# ----------------------------------------------------------------------------------------------------------------------
pygame.init()
frame_clock = pygame.time.Clock()
display = pygame.display.set_mode((SCREEN_W, SCREEN_H))  # Ordered pair (tuple) of screen width and height


# ----------------------------------------------------------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.dimensions = Vector2(50, 50)
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        self.rect.center = (SCREEN_W / 2, SCREEN_H / 2)


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
        self.dimensions = Vector2(640, 100)
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()

        self.rect.bottomleft = (0, SCREEN_H)

        super().__init__()

    def update(self):
        # Code specific to a Platform that will run every frame
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------
        pass


def main():
    # Initialization code - runs only when we start the game
    # ------------------------------------------------------------------------------------------------------------------
    ground = Platform()
    player = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ground)
    all_sprites.add(player)

    # ------------------------------------------------------------------------------------------------------------------

    # Event loop - runs every frame
    # ------------------------------------------------------------------------------------------------------------------
    while True:
        # Code that runs every frame
        display.fill(CYAN)

        # Cycle through all the events (user inputs)
        for event in pygame.event.get():
            # If the event is a quit (X out of the window)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw on the screen
        for sprite in all_sprites:
            display.blit(sprite.image, sprite.rect)

        pygame.display.update()
        frame_clock.tick(FRAMES_PER_SECOND)
    # ------------------------------------------------------------------------------------------------------------------


# Run the main() function. Ignore this - just edit main()
main()
