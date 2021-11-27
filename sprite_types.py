import os
import pygame
import sys
import World
import math


MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)


DECO_GROUP = pygame.sprite.Group()
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

    Health = 1
    Speed = 6

    def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect


    def update(self):

        x = pygame.mouse.get_pos()[0] - World.HEIGHT/2
        y = pygame.mouse.get_pos()[1] - World.WIDTH/2
        self.a = -math.degrees(math.atan2(y, x))

        self.sprite.fill(MAGENTA)
        modded = Main_Character.rot_center(self.boi, self.rect, self.a)[0]

        self.sprite.blit(modded, (0, 0))
        self.rect = Main_Character.rot_center(self.boi, self.rect, self.a)[1]


class Main_Character_Collision(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.Width = 10
        self.Height = 10

        self.image = pygame.Surface([self.Height, self.Width])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))



        self.rect = self.image.get_rect()


Building_IMG = {
    1: "Building-1.png",
    2: "Theehe.png",
    3: "Building-3.png",
    4: "Building-4.png"

}


class Building(pygame.sprite.Sprite):

    def __init__(self, coord_x, coord_y, type):

        super().__init__()

        self.image = pygame.image.load(os.path.join("Assets", Building_IMG.get(type))).convert_alpha()

        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", Building_IMG.get(type))).convert_alpha(), (self.image.get_rect()[2]*4, self.image.get_rect()[3]*4))
        self.rect = self.image.get_rect()

        self.X, self.Y = coord_x, coord_y

    def update(self):
        self.rect.center = (self.X + World.X, self.Y + World.Y)

    def place(self, coord_x, coord_y, type):
        return Building(coord_x, coord_y, type)

class Tree(pygame.sprite.Sprite):

    def __init__(self, coord_x, coord_y, type):

        super().__init__()

        self.multiplier = 3

        self.image = pygame.image.load(os.path.join("Assets", Building_IMG.get(type))).convert_alpha()

        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", Building_IMG.get(type))).convert_alpha(),
            (self.image.get_rect()[2] * self.multiplier, self.image.get_rect()[3] * self.multiplier))
        self.rect = self.image.get_rect()

        self.X, self.Y = coord_x, coord_y

    def update(self):
        self.rect.center = (self.X + World.X, self.Y + World.Y)

    def place(self, coord_x, coord_y, type):
        return Tree(coord_x, coord_y, type)


class Tree_Collision(pygame.sprite.Sprite):

    def __init__(self, coord_x, coord_y, type):

        super().__init__()

        self.png = pygame.image.load(os.path.join("Assets", Building_IMG.get(type))).convert_alpha()

        self.Width = self.png.get_width()
        self.Height = self.png.get_height()

        print(self.Width, self.Height)

        self.image = pygame.Surface([self.Width, self.Height])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.X, self.Y = coord_x, coord_y

    def update(self):
        self.rect.center = (self.X + World.X, self.Y + World.Y)

    def place(self, coord_x, coord_y, type):
        return Tree_Collision(coord_x, coord_y, type)


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

        self.lifetime = pygame.time.get_ticks() + 3000


    def removeBullet(self):
        if pygame.time.get_ticks() >= self.lifetime:
            self.kill()
        if pygame.sprite.spritecollide(self, BUILDINGS_GROUP, dokill=False):
            self.velocity_x = self.velocity_x * -1
            self.velocity_y = self.velocity_y * -1


    def update(self):
        self.pos[0] += self.velocity_x + World.Delta_X
        self.pos[1] += self.velocity_y + World.Delta_Y

        self.rect.center = self.pos
        self.removeBullet()