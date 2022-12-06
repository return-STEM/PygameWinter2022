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
# (NEW) let's set side-scrolling speed to a constant, since we'll use it elsewhere in code
SCROLLING_SPEED = 5

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

        self.rect.center = (SCREEN_W / 4, 120)

        self.velocity = Vector2(0, 0)

        super().__init__()
        super().__init__()

    def update(self):
        # Code specific to a Player that will run every frame
        # --------------------------------------------------------------------------------------------------------------

        self.velocity.y += GRAVITY
        self.rect.center += self.velocity
        # (NEW) restart the game if we fall into a hole
        if self.rect.top > SCREEN_H:
            main()

        # --------------------------------------------------------------------------------------------------------------
        pass


class Platform(pygame.sprite.Sprite):
    def __init__(self, width=SCREEN_W, position=0):
        self.dimensions = Vector2(width, 100)
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()

        self.rect.bottomleft = (position, SCREEN_H)
        # (NEW) side scrolling speed refactor
        self.velocity = Vector2(-SCROLLING_SPEED, 0)

        super().__init__()

    def update(self):
        # Code specific to a Platform that will run every frame
        # --------------------------------------------------------------------------------------------------------------
        self.rect.center += self.velocity
        # (NEW) once the platform goes offscreen, it will clean itself up (delete itself)
        if self.rect.right < 0:
            del self

        # --------------------------------------------------------------------------------------------------------------
        pass


def main():
    # Initialization code - runs only when we start the game
    # ------------------------------------------------------------------------------------------------------------------
    # (NEW) let's add the ground back to give the player a little grace period at the start
    ground = Platform()
    player = Player()

    ground_sprites = pygame.sprite.Group()
    # (NEW) let's add the ground back to give the player a little grace period at the start
    ground_sprites.add(ground)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ground_sprites)
    all_sprites.add(player)

    # (NEW) let's add the ground back to give the player a little grace period at the start
    # Since we now have the ground, don't generate platforms for the first screen
    generator_position = 640

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

        while generator_position < SCREEN_W:
            platform_width = random.randint(80, 160)
            new_platform = Platform(
                width=platform_width, position=generator_position
            )
            ground_sprites.add(new_platform)
            all_sprites.add(new_platform)
            gap_width = random.randint(60, 120)
            generator_position += platform_width
            generator_position += gap_width

        # (NEW) let's make generator_position update while we're scrolling
        generator_position -= SCROLLING_SPEED

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
