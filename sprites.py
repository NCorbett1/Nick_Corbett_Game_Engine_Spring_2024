# This file was created by: Nick Corbett
# This code was inspired by Zelda and informed by Chris Bradfield
import pygame as pg 
from settings import *
#Import pygame and settings


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = game.all_sprites
        # init super class
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x *TILESIZE
        self.y = y *TILESIZE
#Shows how to play game and what does what
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys = [pg.K_LEFT] or keys[pg.K_a]:
            self.vx = PLAYER SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = PLAYER_SPEED
        if keys[pg/K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx !=0 and self.vy !=0:
            self.vx *= 0.7071
            self.vy *= 0.7071

#This code imports the sizes and basics of the player
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
         self.x += dx
         self.y += dy
    
    def collide_with_walls(self, dx=0, dy=0)
        for wall in self.game.walls:
            if wall.x == slef.x + dx and wall.y == self.y +dy: 
                return True
            return False
        
#What happens if game collides with walls
def collide_with_walls(self, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if hits: 
            if self.vx > 0: 
                self.x = hits[0].rect.left - self.width
            if self.vx < 0: 
                self.x = hits[0].rect.right
            self.vx = 0
            self.rect.x = self.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if hits: 
            if self.vy > 0: 
                self.y = hits[0].rect.top - self.rect.height
            if self.vy < 0: 
                self.y = hits[0].rect.bottom
            self.vy = 0
            self.rect.y = self.y
    def collide_with_objects(self, group, kill):
        hits= pg.sprite.spritecollide(self, self.game.coins, True)
        if hits:
            return True

#updates system
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt 
        self.y += self.vy * self.game.dt 
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        if self.collide_with_group(self.game.coins, True):
            self.moneybag +=1
        coin_hits = pg.spirte.cpritecollide(self, self.game.coims, True)
        if coin_hits:
            self.moneybag +=1

        
#Line 21 and below initiate the wall with sprites
class Wall(pg.sprite.Sprite): 
        def __init__(self, x, y):
            self.groups = game.all_sprites, game.walls
            pg.sprite.Sprite.__init__(self, self.groups)
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

class Coin(pg.sprite.Sprite): 
        def __init__(self, x, y):
            self.groups = game.all_sprites, game.coins
            pg.sprite.Sprite.__init__(self, self.groups)
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(LIGHTGREY)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE