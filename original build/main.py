# This file was created by: Nick Corbett
#The recent code is from Chat GPT
# import libraries and modules
import pygame as pg
from settings import *
from sprites import *
from random import randint
import sys
from os import path


LEVEL1 = "level1.txt"
LEVEL2 = "level2.txt"

#beta goals, end screen, start scree, working code
#Also add new levels and a charectristic such as something we have never done like an emote after collecting coin 


# Define game class...
class Game:
    # Define a special method to init the properties of said class...
    def __init__(self):
        # init pygame
        pg.init()
        # set size of screen and be the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        # setting game clock 
        self.clock = pg.time.Clock()
        self.load_data()
        
     


    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(self.game_folder, 'level1.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)

    def new(self):
        print("create new game...")
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.boosts = pg.sprite.Group()
        self.superspeeds = pg.sprite.Group()
        # self.player1 = Player(self, 1, 1)
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                #Below are all tiles that are placed into map.txt to run the game
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'F':
                    Mob(self, col, row)
                if tile == 'L':
                    Boost(self, col, row)
                if tile == 'K':
                    SUPERSPEED(self, col, row)


    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(self.game_folder, LEVEL1), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)

    def change_level(self, lvl):
        for s in self.all_sprites:
            s.kill()
        self.player.moneybag = 0
        self.map_data = []
        with open(path.join(self.game_folder, lvl), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                #Below are all tiles that are placed into map.txt to run the game
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'F':
                    Mob(self, col, row)
                if tile == 'L':
                    Boost(self, col, row)
                if tile == 'K':
                    SUPERSPEED(self, col, row)
    
    # def show_start_screen(self):
    #     self.screen.fill(BGCOLOR)
    #     self.draw_text(self.screen, "The Beginning", 24, WHITE, 10, 2)
    #     pg.display.flip()
    #     self.wait_for_key()


    def wait_for_key(self):
        waiting = True
        while waiting: 
            self.clock.tick(FPS) 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False
    # Create run method which runs the whole GAME

    def run(self):
        # runs the game and allows the game to quit 
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            self.check_wall_collision()

    def check_wall_collision(self):
        # Check collision between player and walls
        hits = pg.sprite.spritecollide(self.player, self.walls, False)
        for wall in hits:
            wall.color_timer = 180  # Change wall color for 3 seconds (60 FPS * 3 seconds)

    def quit(self):
         pg.quit()
         sys.exit() 
#updates game
    def update(self):
        self.all_sprites.update()
        if self.player.moneybag > 8:
            self.change_level(LEVEL2)
    #size of game and boxes on the screen
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
#rules of quitting game
    def events(self):
         for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_LEFT:
            #         self.player.move(dx=-1)
            #     if event.key == pg.K_RIGHT:
            #         self.player.move(dx=1)
            #     if event.key == pg.K_UP:
            #         self.player.move(dy=-1)
            #     if event.key == pg.K_DOWN:
            #         self.player.move(dy=1)

    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('comicsans')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)

    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.screen, "The Beginning", 24, WHITE, 10, 2)
        pg.display.flip()
        self.wait_for_key()

# Instantiate the game... 
g = Game()
g.show_start_screen()
# use game method run to run
# g.show_start_screen()
while True:
    g.new()
    g.run()
    # g.show_go_screen()


