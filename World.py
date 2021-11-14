import os
import pygame
import sys

WIDTH, HEIGHT = 1080, 1920
X = 0
Y = 0

Last_X = X
Last_Y = Y

Delta_X = 0
Delta_Y = 0

def find_delta():
    global Delta_X
    global Delta_Y
    Delta_X = X - Last_X
    Delta_Y = Y - Last_Y

#nekreipkit demesio, del bendros tavrkos padariau ir world faila