import os
import pygame
import sys
import World

WHITE = (255, 255, 255)

BUILDINGS_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()
NPC_GROUP = pygame.sprite.Group()

class Main_Character(pygame.sprite.Sprite):


    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent


        try:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "dood_right2.png")), (Main_Character.Width, Main_Character.Height)).convert_alpha()
        except:
            pass
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    Rotation = [False, False, False, False, False]
    Width = 55
    Height = 103

    Speed = 3


class Building(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, coord_x, coord_y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load(os.path.join("Assets", "House1.png")).convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        Building.X, Building.Y = coord_x, coord_y

    def update(self):
        self.rect.center = (Building.X + World.X, Building.Y + World.Y)

    X, Y = 0, 0
#https://www.youtube.com/watch?v=hDu8mcAlY4E&ab_channel=ClearCode

#https://www.youtube.com/watch?v=jO6qQDNa2UY&t=2387s&ab_channel=TechWithTim

