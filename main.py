# This file was created by: Nick Corbett
#first file commit from VS Code
#Imports pygame as pg and imports settings code
#Goal 1: mob
#Goal 2: coins
#Goals 3: game over
import pygame as pg 
from settings import *
from sprites import *
from random import randint
import sys
from os import path
#creates a variable called game
#this makes something new
class Game:
#code template for creating python
    def __init__(self):
        # initiate self
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TILE)
        #set game clock
        self.clock = pg.time.Clock()
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path,join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                
   #create way to run whole game    
    def new(self):
    # sets size of player
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.player1= Player(self, 1, 1)
        self.mob
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
                print(row)
                for col, tile in enumerate(tiles):
                    print(col)
                    if tile == '1':
                        print("a wall at", row, col)
                        Wall(self, col, row)
                
#why does this go there
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
#imports clock and settings
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def quit(self):
        pg.quit()   
        sys.exit()
#will update sprites and changes
    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
#parameters for game
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_LEFT:
        #         self.player1.move(dx=-1)
#Instantiate the game...
g = Game()
#use game method run to run
#g.show_start_screen
while True:
    g.new()
    g.run()
    #g.show_go_screen()


        