import os
import pygame
import sys

class Main_Player(pygame.sprite.Sprite):  #Cia piesiu visus spritus
    def __init__(self, width, height, pos_x, pos_y, color):
        #super().__init__()
        self.image = pygame.surface([width, height]) #gali buti ir [] sklaiustai
        self.image.fill(color)
        self.rect = self.image.get_rect()

#https://www.youtube.com/watch?v=hDu8mcAlY4E&ab_channel=ClearCode

#https://www.youtube.com/watch?v=jO6qQDNa2UY&t=2387s&ab_channel=TechWithTim

pygame.surface()