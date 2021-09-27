import os
import pygame
import sys
import sprite_types

pygame.font.init()

class World:
    X = 0
    Y = 0

BUILDINGS = pygame.sprite.Group()

class Player:
    def __init__(self, PWIDTH, PHEIGHT):
        self.width = PWIDTH
        self.height = PHEIGHT

    def main(self, display):
        pygame.draw.rect(display, (0, 255, 0), (HEIGHT/2-Player.Height/4, WIDTH/2-Player.Width/2, self.width, self.height))

    def collision(self):
        if pygame.sprite.spritecollide(True, BUILDINGS):
            if Player.Rotation == 1:
                World.Y += Player.Speed
            if Player.Rotation == 2:
                World.X += Player.Speed
            if Player.Rotation == 3:
                World.Y += -Player.Speed
            if Player.Rotation == 4:
                World.X += -Player.Speed

    Rotation = 1
    Width = 55
    Height = 103

    Speed = 2.5

WIDTH, HEIGHT = 1080, 1920  #Standartiniai apsirasymai, net neklausk, self explanatory
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption("AMBICIJA")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "icon.png")))

FONT = pygame.font.Font(os.path.join("Assets", "kongtext.ttf"), 32)

BLACK = (0, 0, 0)
GREEN = (0, 255, 100)


APPLE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Apple.png")), (44, 52)).convert_alpha()
DOOD = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "dood_right2.png")), (Player.Width, Player.Height)).convert_alpha()
HOUSE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "House_object.png")), (163*3, 228*3)).convert_alpha()
TEST_GRASS2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "map 1.1.png")), (4244*3, 3000*3)).convert()

def draw_window(): #Visi piesiami dalykai eina cia <3
    WIN.blit(TEST_GRASS2, (0 + World.X, 0 + World.Y))
    WIN.blit(APPLE, (100+World.X, 600+World.Y))
    HOUSE1_rect = pygame.Rect(200 + World.X, 0 + World.Y, 163 * 3, 228 * 3)
    pygame.draw.rect(WIN, BLACK, HOUSE1_rect)
    """if World.Y > -50:
        WIN.blit(DOOD, (HEIGHT / 2 - Player.Height / 4, WIDTH / 2 - Player.Width / 2))
        WIN.blits([(HOUSE, (200+ World.X, 0+World.Y)), (APPLE, (800+ World.X, 800+World.Y))])
    else:
        WIN.blits([(HOUSE, (200 + World.X, 0 + World.Y)), (APPLE, (800 + World.X, 800 + World.Y))])
        WIN.blit(DOOD, (HEIGHT / 2 - Player.Height / 4, WIDTH / 2 - Player.Width / 2))"""
    WIN.blit(FONT.render( str(int(clock.get_fps())), True, (255, 255, 255, 255), (0, 0, 0, 255)), (1850, 6))


def controls():
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w]:    #Virsus
        World.Y += Player.Speed
        Player.Rotation = 3
    if keypress[pygame.K_s]:    #Apacia
        World.Y += -Player.Speed
        Player.Rotation = 1
        print(World.Y)
    if keypress[pygame.K_a]:    #Kaire
        World.X += Player.Speed
        Player.Rotation = 2
    if keypress[pygame.K_d]:    #Desine
        World.X += -Player.Speed
        Player.Rotation = 4


main_player = sprite_types.Main_Player(Player.Width, Player.Height, HEIGHT / 2 - Player.Height, WIDTH / 2 - Player.Width, BLACK)

player = Player(Player.Width, Player.Height)


def main():  # Main loop'as check'ina visus eventus programoje for example QUIT

    #gali buti, kad rect apverstas

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        controls()
        player.main(WIN)
        draw_window()
        fps_val = str(clock.get_fps())


        pygame.display.update()
        pygame.display.flip()

    sys.exit()
    pygame.quit()

if __name__ == "__main__": # Patikrina ar failas nebuvo importuotas
    main()