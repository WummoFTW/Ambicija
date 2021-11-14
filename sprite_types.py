import os
import pygame
import sys
import World
import math

MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)

BUILDINGS_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()
PLAYER_COLLISION = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()
NPC_GROUP = pygame.sprite.Group()

class Main_Character(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.Width = 12*3
        self.Height = 24*3

        self.boi = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TEST BOI.png")).convert_alpha(), (self.Width, self.Height))

        self.sprite = pygame.Surface((100, 100))

        self.sprite.set_colorkey(MAGENTA)

        self.image = self.sprite
        self.rect = self.sprite.get_rect()

    Rotation = [False, False, False, False, False]

    Speed = 6

    def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image

    def rot_center_rect(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_rect

    def update(self):

        x = pygame.mouse.get_pos()[0] - World.HEIGHT/2
        y = pygame.mouse.get_pos()[1] - World.WIDTH/2
        self.a = -math.degrees(math.atan2(y, x))

        self.sprite.fill(MAGENTA)
        modded = Main_Character.rot_center(self.boi, self.rect, self.a)

        self.sprite.blit(modded, (0, 0))
        self.rect = Main_Character.rot_center_rect(self.boi, self.rect, self.a)


class Main_Character_Collision(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.Width = 36
        self.Height = 36

        self.image = pygame.Surface([self.Height, self.Width])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))

        pygame.draw.rect(self.image, (255, 255, 255), [0, 0, 150, 20])

        self.rect = self.image.get_rect()
        print(self.rect)

Building_IMG = {
    1: "House1.png",
    2: "Trees-2.png"

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




class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        super().__init__()
        # PASUKALIOJAM IR SUTVARKOM
        self.image = pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "Bullet.png")), angle)
        self.rect = self.image.get_rect()
        speed = 20
        # TRIGONOMETRIJA XD
        self.velocity_x = math.cos(math.radians(-angle)) * speed
        self.velocity_y = math.sin(math.radians(-angle)) * speed

        self.pos = list(pos)


    def update(self):
        """REIKIA NEPAMIRST JU NUZUDYT KADA NORS"""
        self.pos[0] += self.velocity_x + World.Delta_X
        self.pos[1] += self.velocity_y + World.Delta_Y

        self.rect.center = self.pos


