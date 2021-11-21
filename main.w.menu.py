import os
import pygame
import sys
import sprite_types
import World

pygame.font.init()

WIDTH, HEIGHT = 1080, 1920  #Standartiniai apsirasymai, net neklausk, self explanatory
WIN = pygame.display.set_mode((HEIGHT, WIDTH), pygame.FULLSCREEN)
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption("AMBICIJA")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "icon.png")))
pygame.mouse.set_visible(False)
FONT = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 16)
smallFont = pygame.font.Font(os.path.join("Assets", "8-BIT WONDER.ttf"), 16)
mediumFont = pygame.font.Font(os.path.join("Assets", "8-BIT WONDER.ttf"), 40)
largeFont = pygame.font.Font(os.path.join("Assets", "8-BIT WONDER.ttf"), 60)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)
RED = (255, 0, 0)

Player = sprite_types.Main_Character()
Player.rect.center = (HEIGHT / 2, WIDTH / 2)

Player_Collision = sprite_types.Main_Character_Collision()
Player_Collision.rect.center = (HEIGHT / 2, WIDTH / 2)

sprite_types.PLAYER_GROUP.add(Player)
sprite_types.PLAYER_COLLISION.add(Player_Collision)

Pastatas = sprite_types.Building(2000, 2000, 1)

sprite_types.BUILDINGS_GROUP.add(Pastatas)

HP_BAR = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "HP_bar.png")), (224*2, 16*2)).convert()
CURSOR = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Cursor.png")), (9*2, 9*2)).convert_alpha()
TEST_GRASS2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Level_1.png")), (3640*2, 2160*2)).convert()


def Mainmenu():
    intro = True
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


def draw_window(): #Piesiamos dekoracijos
    WIN.blit(TEST_GRASS2, (0 + World.X, 0 + World.Y))


def draw_UI():
    WIN.blit(HP_BAR, (1464,1040),(0,0,448,32))
    pygame.draw.rect(WIN, GREEN, pygame.Rect(1515, 1046, 390*Player.Health, 20))
    WIN.blit(CURSOR, (pygame.mouse.get_pos()[0] - 9, pygame.mouse.get_pos()[1] - 9))


def show_info():
    WIN.blit(FONT.render(str(int(clock.get_fps())), True, (255, 255, 255, 255), (0, 0, 0, 255)), (1882, 6))
    WIN.blit(FONT.render(str(str(World.X) + " " + str(World.Y)), True, (255, 255, 255, 255), (0, 0, 0, 255)), (4, 1060))


def controls():
    global keypress
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w]:    #Virsus
        World.Y += Player.Speed
        Player.Rotation[3] = True
    else:
        Player.Rotation[3] = False

    if keypress[pygame.K_s]:    #Apacia
        World.Y += -Player.Speed
        Player.Rotation[1] = True
    else:
        Player.Rotation[1] = False

    if keypress[pygame.K_a]:    #Kaire
        World.X += Player.Speed
        Player.Rotation[2] = True
    else:
        Player.Rotation[2] = False

    if keypress[pygame.K_d]:    #Desine
        World.X += -Player.Speed
        Player.Rotation[4] = True
    else:
        Player.Rotation[4] = False

    left, middle, right = pygame.mouse.get_pressed()
    if left:
        bullet = sprite_types.Bullet(Player.rect.center, Player.a)
        sprite_types.BULLETS.add(bullet)

    if keypress[pygame.K_ESCAPE]: #ESC
        pause()


def collision():
    keypress = pygame.key.get_pressed()
    if pygame.sprite.spritecollideany(Player_Collision, sprite_types.BUILDINGS_GROUP) and Player.Rotation[0] != True:
        if Player.Rotation[1]:    #Apacia
            World.Y += Player.Speed

        if Player.Rotation[2]:    #Kaire
            World.X += -Player.Speed

        if Player.Rotation[3]:    #Virsus
            World.Y += -Player.Speed

        if Player.Rotation[4]:    #Desine
            World.X += Player.Speed


def main():  # Main loop'as check'ina visus eventus programoje for example QUIT

    sprite_types.BUILDINGS_GROUP.add(Pastatas.place(2500, 1000, 3))
    sprite_types.BUILDINGS_GROUP.add(Pastatas.place(3200, 1600, 1))
    sprite_types.BUILDINGS_GROUP.add(Pastatas.place(1200, 1300, 2))
    sprite_types.BUILDINGS_GROUP.add(Pastatas.place(1250, 1000, 2))
    sprite_types.BUILDINGS_GROUP.add(Pastatas.place(1846, 1050, 2))

    World.X = -1000
    World.Y = -1000
    gameOver = False
    run = True

    while gameOver == True: # zaidejas mirsta
        pygame.display.fill(BLACK)
        msg_text("Game Over", RED, y_displace=-50, size="large")
        msg_text("Press R to restart or ESC to quit", WHITE, y_displace=50, size="meidum")
        pygame.display.update()
        if keypress[pygame.K_r]:
            main()
        if keypress[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            gameOver = False

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        World.Last_X = World.X
        World.Last_Y = World.Y
        collision()
        controls()

        WIN.fill((50, 50, 50))
        draw_window()

        sprite_types.BULLETS.update()
        sprite_types.BULLETS.draw(WIN)
        sprite_types.BUILDINGS_GROUP.update()
        sprite_types.BUILDINGS_GROUP.draw(WIN)
        sprite_types.PLAYER_COLLISION.update()
        sprite_types.PLAYER_COLLISION.draw(WIN)
        sprite_types.PLAYER_GROUP.update()
        sprite_types.PLAYER_GROUP.draw(WIN)
        show_info()
        draw_UI()

        World.find_delta()
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__": # Patikrina ar failas nebuvo importuotas
    Mainmenu()
    main()