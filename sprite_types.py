import os
import pygame
import sys
import World
import math
import random

pygame.font.init()

MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)

FONT = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 16)


LOWER_DECO_GROUP = pygame.sprite.Group()
DECO_GROUP = pygame.sprite.Group()
BUILDINGS_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()
PLAYER_COLLISION = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()
NPC_GROUP = pygame.sprite.Group()
BUTTON_GROUP = pygame.sprite.Group()

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


class Legs(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface((100, 100))
        self.image_modded = self.image
        self.image.fill(MAGENTA)
        self.image.set_colorkey(MAGENTA)
        self.image_modded.set_colorkey(MAGENTA)

        self.img = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Char_1.png")).convert_alpha(), (1054*3, 916*3))
        self.Sprites = {
            1: (790*3, 695*3, 27*3, 15*3),
            2: (790*3, 728*3, 27*3, 15*3),
            3: (790*3, 761*3, 27*3, 15*3),
            4: (790*3, 793*3, 27*3, 15*3),
            5: (790*3, 827*3, 27*3, 15*3),
            6: (790*3, 860*3, 27*3, 15*3),
            7: (790*3, 893*3, 27*3, 15*3),
            8: (826 * 3, 628 * 3, 27 * 3, 15 * 3),
            9: (858 * 3, 628 * 3, 27 * 3, 15 * 3),
            10: (890 * 3, 628 * 3, 27 * 3, 15 * 3),
            11: (922 * 3, 628 * 3, 27 * 3, 15 * 3),
            12: (954 * 3, 628 * 3, 27 * 3, 15 * 3),
            13: (986 * 3, 628 * 3, 27 * 3, 15 * 3),
            14: (1018 * 3, 628 * 3, 27 * 3, 15 * 3),
        }
        self.Rotation = [False, False, False, False, False]
        self.x = 0
        self.a = 0
        self.rect = self.image.get_rect()

    def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect

    def update(self):

        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_w] or keypress[pygame.K_a] or keypress[pygame.K_s] or keypress[pygame.K_d]:  # Virsus
            self.x += 0.5
            if self.x > 14:
                self.x = 1
            self.image.fill(MAGENTA)
            self.image.blit(self.img, (9.5, 27.5), self.Sprites.get(round(self.x)))
            self.image_modded = pygame.transform.rotate(self.image, self.a)



        self.image = self.image_modded





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
    2: "Tree_1.png",
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
        return Building(coord_x+960, coord_y+540, type)

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
        return Tree(coord_x+960, coord_y+540, type)


class Tree_Collision(pygame.sprite.Sprite):
    def __init__(self, coord_x, coord_y, type):

        super().__init__()

        self.png = pygame.image.load(os.path.join("Assets", Building_IMG.get(type))).convert_alpha()

        self.Width = self.png.get_width()
        self.Height = self.png.get_height()



        self.image = pygame.Surface([self.Width, self.Height])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.X, self.Y = coord_x, coord_y

    def update(self):
        self.rect.center = (self.X + World.X, self.Y + World.Y)

    def place(self, coord_x, coord_y, type):
        return Tree_Collision(coord_x+960, coord_y+540, type)


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
            self.velocity_x = self.velocity_x * -1 + random.randint(-2, 2)
            self.velocity_y = self.velocity_y * -1 + random.randint(-2, 2)

    def update(self):
        self.pos[0] += self.velocity_x + World.Delta_X
        self.pos[1] += self.velocity_y + World.Delta_Y

        self.rect.center = self.pos
        self.removeBullet()

class Button(pygame.sprite.Sprite):

    def __init__(self, coord_x, coord_y, size_x, size_y, text=''):

        super().__init__()

        self.sprite = pygame.Surface((size_x, size_y))
        self.sprite.blit(FONT.render(text, True, (255, 255, 255, 255), (0, 0, 0, 255)), (0, 0))
        self.sprite.set_colorkey(MAGENTA)

        self.image = self.sprite
        self.rect = self.sprite.get_rect()
        self.rect.center = (coord_x, coord_y)


    def update(self):
        left, middle, right = pygame.mouse.get_pressed()
        if self.rect.collidepoint(pygame.mouse.get_pos()[0] - 9, pygame.mouse.get_pos()[1]) and left:
            self.kill()

    def place(self, coord_x, coord_y, size_x, size_y, text=''):
        return Button(coord_x, coord_y, size_x, size_y, text)
