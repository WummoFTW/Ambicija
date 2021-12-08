import os
import pygame
import main
import sys


def Mainmenu():
    intro = True
    keypress = pygame.key.get_pressed()
    while intro:
        if keypress[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keypress[pygame.K_e]:
            intro = False

        pygame.display.fill(BLACK)
        msg_text("AMBICIJA", WHITE, -70, size="large")
        msg_text("Press E to play", WHITE, 0 , size="medium")
        msg_text("Press ESC to quit", WHITE, 70, size="small")
        pygame.display.update()
        #clock.tick(15)

def pause():
    paused = True
    keypress = pygame.key.get_pressed()
    while paused:
        if keypress[pygame.K_BACKSPACE]:
            pygame.quit()
            sys.exit()
        if keypress[pygame.K_ESCAPE]:
            paused=False

        pygame.display.fill(BLACK)
        msg_text("Paused", WHITE, -100, size="large")
        msg_text("Press C to continue or Q to quit.", WHITE, 25)
        pygame.display.update()
        #clock.tick(5)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallFont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumFont.render(text, True, color)
    elif size == "large":
        textSurface = largeFont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def msg_text(msg, color, y_displace=0, size = "medium"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (WIDTH/2),(HEIGHT/2)+y_displace
    pygame.display.blit(textSurf,textRect)