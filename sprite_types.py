import os
import pygame
import sys

class Main_Player(pygame.sprite.Sprite):  #Cia piesiu visus spritus
    def __init__(self, width, height, pos_x, pos_y, color):
        #super().__init__()
        self.image = pygame.surface([width, height]) #gali buti ir [] sklaiustai
        self.image.fill(color)
        self.rect = self.image.get_rect()