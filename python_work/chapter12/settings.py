"""Import os and sys to get the images"""
import os
import sys

import pygame

path = os.path.join(sys.path[0])
images_path = f"{path}/images/"

"""Docstring for VScode"""
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        back_ground = pygame.image.load(f"{images_path}/bg.png")
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        self.back_ground = pygame.transform.scale(back_ground, (self.screen_width, self.screen_height))
        self.game_display = pygame.display.set_mode((self.screen_width, self.screen_height))

        #self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
