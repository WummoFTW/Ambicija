import os
import pygame
import sys
import sprite_types
import World


pygame.font.init()

WIDTH, HEIGHT = 1080, 1920  #Standartiniai apsirasymai, net neklausk, self explanatory
#WIN = pygame.display.set_mode((HEIGHT, WIDTH))
WIN = pygame.display.set_mode((HEIGHT, WIDTH), pygame.FULLSCREEN)
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption("AMBICIJA")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "icon.png")))
pygame.mouse.set_visible(False)
FONT = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 16)
smallFont = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 16)
mediumFont = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 40)
largeFont = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 60)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)
RED = (255, 0, 0)

Player = sprite_types.Main_Character()
Player.rect.center = (HEIGHT / 2, WIDTH / 2)
sprite_types.PLAYER_GROUP.add(Player)

Player_Collision_1 = sprite_types.Main_Character_Collision()
Player_Collision_1.rect.center = (HEIGHT / 2, WIDTH / 2-10)
sprite_types.PLAYER_COLLISION.add(Player_Collision_1)

Player_Collision_2 = sprite_types.Main_Character_Collision()
Player_Collision_2.rect.center = (HEIGHT / 2-10, WIDTH / 2)
sprite_types.PLAYER_COLLISION.add(Player_Collision_2)

Player_Collision_3 = sprite_types.Main_Character_Collision()
Player_Collision_3.rect.center = (HEIGHT / 2, WIDTH / 2+10)
sprite_types.PLAYER_COLLISION.add(Player_Collision_3)

Player_Collision_4 = sprite_types.Main_Character_Collision()
Player_Collision_4.rect.center = (HEIGHT / 2+10, WIDTH / 2)
sprite_types.PLAYER_COLLISION.add(Player_Collision_4)




Pastatas = sprite_types.Building(2000, 2000, 1)
Medis = sprite_types.Tree(2000, 2000, 1)
Medis_collision = sprite_types.Tree_Collision(2000, 2000, 1)



HP_BAR = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "HP_bar.png")), (448*2, 16*2)).convert()
CURSOR = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Cursor.png")), (9*2, 9*2)).convert_alpha()
TEST_GRASS2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Level_1.png")), (3640*2, 2160*2)).convert()

def pause():
    paused = True
    WIN.fill(BLACK)
    msg_text("Paused", WHITE, -100, size="large")
    msg_text("Press Backspace to continue", WHITE, 25)
    msg_text("Or q to quit the game.", WHITE, 85)
    msg_text("m to go back to main menu", WHITE, 150, size="small")
    pygame.display.update()

    while paused==True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_m:
                    Mainmenu()


def Mainmenu():
    intro = True
    WIN.fill(BLACK)
    msg_text("AMBICIJA", WHITE, -130, size="large")
    msg_text("Press E to play", WHITE, 0, size="medium")
    msg_text("Press ESC to quit", WHITE, 60, size="small")
    pygame.display.update()

    while intro==True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    level_select()
                    intro = False
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def level_select():
    Lvl_sel = True
    WIN.fill(BLACK)
    msg_text("Select Level", WHITE, -130, size="large")
    msg_text("Level 1 - Press 1", WHITE, 0, size="medium")
    msg_text("Level 2 - Press 2", WHITE, 40, size="medium")
    msg_text("Level 3 - Press 3", RED, 80, size="medium")
    msg_text("ESACAPE to go back", WHITE, 120, size="small")
    pygame.display.update()

    while Lvl_sel == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Lvl_sel = False
                    World.Level = 1
                    main()
                if event.key==pygame.K_2:
                    Lvl_sel = False
                    World.Level = 2
                    main()
                if event.key==pygame.K_3:
                    Lvl_sel = False
                    World.Level = 3
                    main()
                if event.key==pygame.K_ESCAPE:
                    Lvl_sel = False
                    Mainmenu()
                    

def msg_text(msg, color, y_displace=0, size = "medium"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (HEIGHT/2),(WIDTH/2)+y_displace  #Menu, Pause, Gameover text pozicija
    WIN.blit(textSurf,textRect)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallFont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumFont.render(text, True, color)
    elif size == "large":
        textSurface = largeFont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def draw_window(): #Piesiamos dekoracijos
    WIN.blit(TEST_GRASS2, (0 + World.X, 0 + World.Y))


def draw_UI():
    WIN.blit(HP_BAR, (1464, 1040), (0, 0, 448, 32))
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

    if keypress[pygame.K_ESCAPE]: #Pauzė
        pause()


    left, middle, right = pygame.mouse.get_pressed()
    if left:
        bullet = sprite_types.Bullet(Player.rect.center, Player.a)
        sprite_types.BULLETS.add(bullet)


def collision():
    if pygame.sprite.spritecollideany(Player_Collision_1, sprite_types.BUILDINGS_GROUP):
        World.Y += -Player.Speed

    if pygame.sprite.spritecollideany(Player_Collision_2, sprite_types.BUILDINGS_GROUP):
        World.X += -Player.Speed

    if pygame.sprite.spritecollideany(Player_Collision_3, sprite_types.BUILDINGS_GROUP):
        World.Y += Player.Speed

    if pygame.sprite.spritecollideany(Player_Collision_4, sprite_types.BUILDINGS_GROUP):
        World.X += Player.Speed


def Level(lvl):
    try:
        path = str(lvl) + ".lvl"

        f = open(path, 'r').readlines()

        for x in range(len(f)):

            data = f[x].split()
            print(data)

            if int(data[0]) == 1:
                sprite_types.BUILDINGS_GROUP.add(Pastatas.place(int(data[1]), int(data[2]), int(data[3])))
            elif int(data[0]) == 2:
                sprite_types.BUILDINGS_GROUP.add(Medis_collision.place(int(data[1]), int(data[2]), int(data[3])))
                sprite_types.DECO_GROUP.add(Medis.place(int(data[1]), int(data[2]), int(data[3])))

    except:
        quit("Level is not generated yet")

    '''
    sprite_types.DECO_GROUP.add(Medis.place(0, 0, 2))
    sprite_types.BUILDINGS_GROUP.add(Medis_collision.place(0, 0, 2))

    sprite_types.BUILDINGS_GROUP.add(Pastatas.place(2200, 1600, 1))

    sprite_types.DECO_GROUP.add(Medis.place(1200, 1300, 2))
    sprite_types.BUILDINGS_GROUP.add(Medis_collision.place(1200, 1300, 2))
    sprite_types.DECO_GROUP.add(Medis.place(1250, 1000, 2))
    sprite_types.BUILDINGS_GROUP.add(Medis_collision.place(1250, 1000, 2))
    sprite_types.DECO_GROUP.add(Medis.place(1846, 1050, 2))
    sprite_types.BUILDINGS_GROUP.add(Medis_collision.place(1846, 1050, 2))
    '''

'''
    if Player.Health == 0:  #sorry for the trash kol kas. Gal prireiks (Health not defined) (Man atrodo pataisiau -Karolis)
        gameOver = True
    while gameOver == True: # zaidejas mirsta
        WIN.fill(BLACK)
        msg_text("Game Over", RED, y_displace=-50, size="large")
        msg_text("Press R to restart or ESC to quit", WHITE, y_displace=50, size="meidum")
        WIN.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameOver=False
                    main()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
'''

def main():  # Main loop'as check'ina visus eventus programoje for example QUIT
    Level(World.Level)

    World.X = -100
    World.Y = -100


    run = True
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

        sprite_types.PLAYER_GROUP.update()
        sprite_types.PLAYER_GROUP.draw(WIN)

        sprite_types.BUILDINGS_GROUP.update()
        sprite_types.BUILDINGS_GROUP.draw(WIN)

        sprite_types.DECO_GROUP.update()
        sprite_types.DECO_GROUP.draw(WIN)

        sprite_types.PLAYER_COLLISION.update()
        sprite_types.PLAYER_COLLISION.draw(WIN)

        show_info()
        draw_UI()

        World.find_delta()
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__": # Patikrina ar failas nebuvo importuotas
    Mainmenu()
    #main()
