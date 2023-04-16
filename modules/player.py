import pygame as pg
from settings import *

class Player():
    def __init__(self):
        self.sprites = [pg.image.load(f'assets/sprites/playerWalk{i}.png').convert_alpha() for i in range(2)]
        self.scale = self.sprites[0].get_width() * SPRITE_SCALE, self.sprites[0].get_height() * SPRITE_SCALE
        self.sprites = [pg.transform.scale(sprite, self.scale) for sprite in self.sprites]
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = 1*TILE_SIZE
        self.rect.y = 2*TILE_SIZE
        self.is_moving = False
        self.is_mine = False
        self.animation_timer = 0
        self.animation_index = 0
        self.orientation = 1
        self.gravity = 250

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, floor):
        if(floor[int(self.rect.y/TILE_SIZE+1)][int((self.rect.x/TILE_SIZE))] != 1):
            floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE))] = 0
            floor[int(self.rect.y/TILE_SIZE+1)][int((self.rect.x/TILE_SIZE))] = 9
            self.rect.y += TILE_SIZE
            
        if self.is_moving:
            if self.orientation == 1:
                if(floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)+1)] != 1):
                    floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE))] = 0
                    floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)+1)] = 9
                    self.rect.x += TILE_SIZE
            elif self.orientation == 0:
                if(floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)-1)] != 1):
                    floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE))] = 0
                    floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)-1)] = 9
                    self.rect.x -= TILE_SIZE
            self.animation_index = 1
            self.animation_timer = pg.time.get_ticks() + ANIMATION_PLAYER_MOVE
            self.is_moving = False

        if self.is_mine:
            if self.orientation == 1:
                if(floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)+1)] == 1):
                    floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)+1)] = 0
                elif(floor[int(self.rect.y/TILE_SIZE+1)][int((self.rect.x/TILE_SIZE)+1)] == 1):
                    floor[int(self.rect.y/TILE_SIZE+1)][int((self.rect.x/TILE_SIZE)+1)] = 0
            elif self.orientation == 0:
                if(floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)-1)] == 1):
                    floor[int(self.rect.y/TILE_SIZE)][int((self.rect.x/TILE_SIZE)-1)] = 0
                elif(floor[int(self.rect.y/TILE_SIZE+1)][int((self.rect.x/TILE_SIZE)-1)] == 1):
                    floor[int(self.rect.y/TILE_SIZE+1)][int((self.rect.x/TILE_SIZE)-1)] = 0
            self.is_mine = False

        if self.animation_timer > pg.time.get_ticks():
            self.image = self.sprites[self.animation_index]
        else:
            self.image = self.sprites[0]

    def check_events(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            self.is_moving = True
            self.orientation = 1
        elif event.type == pg.KEYDOWN and event.key == pg.K_a:
            self.is_moving = True
            self.orientation = 0
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            self.is_mine = True
