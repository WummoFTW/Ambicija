import os
import pygame
import sys
import World


WHITE = (255, 255, 255)

BUILDINGS_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()
PLAYER_COLLISION = pygame.sprite.Group()
NPC_GROUP = pygame.sprite.Group()

class Main_Character(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.SHEET = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Main_sprite_sheet.bmp")).convert_alpha(), (96*3, 96*3))

        self.sprite = pygame.Surface((Main_Character.Width, Main_Character.Height))
        self.sprite.set_colorkey((0, 0, 0))
        self.sprite.blit(self.SHEET, (0, 0), (0, 48*3, 48*3, 48*3))
        self.image = self.sprite
        self.rect = self.sprite.get_rect()

    Rotation = [False, False, False, False, False]
    Width = 48*3
    Height = 48*3

    Speed = 6

    def update(self):
        if Main_Character.Rotation[2]==True:
            self.sprite.fill((0,0,0))
            self.sprite.blit(self.SHEET, (0, 0), (48*3, 0, 48*3, 48*3))
        if Main_Character.Rotation[4]==True:
            self.sprite.fill((0,0,0))
            self.sprite.blit(self.SHEET, (0, 0), (0, 0, 48*3, 48*3))
        if Main_Character.Rotation[1]==True:
            self.sprite.fill((0,0,0))
            self.sprite.blit(self.SHEET, (0, 0), (0, 48*3, 48*3, 48*3))
        if Main_Character.Rotation[3]==True:
            self.sprite.fill((0,0,0))
            self.sprite.blit(self.SHEET, (0, 0), (48*3, 48*3, 48*3, 48*3))


class Main_Character_Collision(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface([72, 20])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))

        pygame.draw.rect(self.image, (255, 255, 255), [0, 0, 150, 20])

        self.rect = self.image.get_rect()
        print(self.rect)

Building_IMG = {
    1: "House1.png",
    2: "Swing.png"

}


class Building(pygame.sprite.Sprite):

    def __init__(self, coord_x, coord_y, type):

        super().__init__()

        self.image = pygame.image.load(os.path.join("Assets", Building_IMG.get(type))).convert_alpha()

        self.rect = self.image.get_rect()

        self.X, self.Y = coord_x, coord_y

    def update(self):
        self.rect.center = (self.X + World.X, self.Y + World.Y)

    def place(self, coord_x, coord_y, type):
        return Building(coord_x, coord_y, type)








# https://www.youtube.com/watch?v=hDu8mcAlY4E&ab_channel=ClearCode

# https://www.youtube.com/watch?v=jO6qQDNa2UY&t=2387s&ab_channel=TechWithTim

