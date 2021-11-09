import os
import pygame
import sys
import sprite_types
import World

pygame.font.init()


WIDTH, HEIGHT = 1080, 1920  #Standartiniai apsirasymai, net neklausk, self explanatory
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption("AMBICIJA")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "icon.png")))
pygame.mouse.set_visible(False)
FONT = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 16)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)

Player = sprite_types.Main_Character()
Player.rect.center = (HEIGHT / 2, WIDTH / 2)

Player_Collision = sprite_types.Main_Character_Collision()
Player_Collision.rect.center = (HEIGHT / 2, WIDTH / 2)



sprite_types.PLAYER_GROUP.add(Player)
sprite_types.PLAYER_COLLISION.add(Player_Collision)

Pastatas = sprite_types.Building(1000, 1000, 1)

sprite_types.BUILDINGS_GROUP.add(Pastatas)

sprite_types.BUILDINGS_GROUP.add(Pastatas.place(0, 1000, 1))
sprite_types.BUILDINGS_GROUP.add(Pastatas.place(0, 0, 2))

APPLE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Apple.png")), (44, 52)).convert_alpha()
CURSOR = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Cursor.png")), (9*2, 9*2)).convert_alpha()
TEST_GRASS2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "map 1.1.png")), (4244*3, 3000*3)).convert()



def draw_window(): #Visi piesiami dalykai eina cia <3
    WIN.blit(TEST_GRASS2, (0 + World.X, 0 + World.Y))
    WIN.blit(CURSOR, (pygame.mouse.get_pos()[0]-9,pygame.mouse.get_pos()[1]-9))



def show_info():
    WIN.blit(FONT.render(str(int(clock.get_fps())), True, (255, 255, 255, 255), (0, 0, 0, 255)), (1850, 6))
    WIN.blit(FONT.render(str(str(World.X) + " " + str(World.Y)), True, (255, 255, 255, 255), (0, 0, 0, 255)), (6, 1040))


def controls():
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



def collision():
    keypress = pygame.key.get_pressed()
    if pygame.sprite.spritecollideany(Player_Collision, sprite_types.BUILDINGS_GROUP) and Player.Rotation[0] != True:
        if Player.Rotation[1] == True:    #Apacia
            World.Y += Player.Speed

        if Player.Rotation[2] == True:    #Kaire
            World.X += -Player.Speed

        if Player.Rotation[3] == True:    #Virsus
            World.Y += -Player.Speed

        if Player.Rotation[4] == True:    #Desine
            World.X += Player.Speed


print(Pastatas.image.get_rect())



def main():  # Main loop'as check'ina visus eventus programoje for example QUIT
    Pastatas.place(10,0,2)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        collision()
        controls()

        WIN.fill((50, 50, 50))
        draw_window()

        sprite_types.BUILDINGS_GROUP.update()
        sprite_types.BUILDINGS_GROUP.draw(WIN)
        sprite_types.PLAYER_COLLISION.update()
        sprite_types.PLAYER_COLLISION.draw(WIN)
        sprite_types.PLAYER_GROUP.update()
        sprite_types.PLAYER_GROUP.draw(WIN)
        show_info()
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__": # Patikrina ar failas nebuvo importuotas
    main()