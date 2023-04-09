import pygame as pg
from settings import *

class Player():
    def __init__(self):
        self.sprites = [pg.image.load(f'assets/sprites/Fire{i}.png').convert_alpha() for i in range(2)]
        self.scale = self.sprites[0].get_width() * SPRITE_SCALE, self.sprites[0].get_height() * SPRITE_SCALE
        self.sprites = [pg.transform.scale(sprite, self.scale) for sprite in self.sprites]
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.is_moving = False
        self.animation_timer = 0
        self.animation_index = 0
        self.orientation = 1
        self.gravity = 250

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, dt, floor):
        for f in floor:
            if self.rect.colliderect(f):
                self.gravity = 0
                break
            else:
                self.gravity = 250
        self.rect.y += self.gravity * dt

        if self.is_moving:
            if self.orientation == 1:
                self.rect.x += TILE_SIZE
            else:
                self.rect.x -= TILE_SIZE
            self.animation_index = 1
            self.animation_timer = pg.time.get_ticks() + ANIMATION_PLAYER_MOVE
            self.is_moving = False

        if self.animation_timer > pg.time.get_ticks():
            self.image = self.sprites[self.animation_index]
        else:
            self.image = self.sprites[0]

    def check_events(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            if self.gravity == 0:
                self.is_moving = True
                self.orientation = 1
        elif event.type == pg.KEYDOWN and event.key == pg.K_a:
            if self.gravity == 0:
                self.is_moving = True
                self.orientation = 0
