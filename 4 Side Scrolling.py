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

# ----------------------------------------------------------------------------------------------------------------------
GRAVITY = 6

# Setting up Pygame
# ----------------------------------------------------------------------------------------------------------------------
pygame.init()
frame_clock = pygame.time.Clock()
display = pygame.display.set_mode((SCREEN_W, SCREEN_H))  # Ordered pair (tuple) of screen width and height


# ----------------------------------------------------------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.dimensions = Vector2(50, 50)
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        # (NEW) Change player starting position
        self.rect.center = (SCREEN_W / 4, 120)

        self.velocity = Vector2(0, 0)

        super().__init__()
        super().__init__()

    def update(self):
        # Code specific to a Player that will run every frame
        # --------------------------------------------------------------------------------------------------------------

        self.velocity.y += GRAVITY
        self.rect.center += self.velocity

        # --------------------------------------------------------------------------------------------------------------
        pass


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        self.dimensions = Vector2(640, 100)
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()

        self.rect.bottomleft = (0, SCREEN_H)
        # (NEW) Move the platforms left to simulate side scrolling
        self.velocity = Vector2(-5, 0)

        super().__init__()

    def update(self):
        # Code specific to a Platform that will run every frame
        # --------------------------------------------------------------------------------------------------------------
        # (NEW) Move the platforms left to simulate side scrolling
        self.rect.center += self.velocity

        # --------------------------------------------------------------------------------------------------------------
        pass


def main():
    # Initialization code - runs only when we start the game
    # ------------------------------------------------------------------------------------------------------------------
    ground = Platform()
    player = Player()

    ground_sprites = pygame.sprite.Group()
    ground_sprites.add(ground)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ground_sprites)
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
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # Jump! but first, make sure the player is touching the ground:
                    hits = pygame.sprite.spritecollide(player, ground_sprites, False)
                    if hits:
                        player.velocity.y += -50

        for sprite in all_sprites:
            sprite.update()

        hits = pygame.sprite.spritecollide(player, ground_sprites, False)
        # If we see a hit
        if hits:
            # Set player vertical velocity to zero
            player.velocity.y = 0
            # Set player vertical position to 1 pixel above where the hit happened
            player.rect.bottom = hits[0].rect.top + 1

        # Draw on the screen
        for sprite in all_sprites:
            display.blit(sprite.image, sprite.rect)

        pygame.display.update()
        frame_clock.tick(FRAMES_PER_SECOND)
    # ------------------------------------------------------------------------------------------------------------------


# Run the main() function. Ignore this - just edit main()
main()
