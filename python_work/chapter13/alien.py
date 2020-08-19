"""Import os and sys to get the images"""
import os
import sys

import pygame
from pygame.sprite import Sprite

path = os.path.join(sys.path[0])
images_path = f"{path}/images/"

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load(f"{images_path}/green_alien.png")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x_pos = float(self.rect.x)