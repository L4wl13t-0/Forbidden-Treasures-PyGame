import pygame as pg
from settings import *
import numpy as np

class Floor():
    def __init__(self, x, y, level):
        self.level = level
        self.floors = self.randomSeed(x, y)
        self.dirtImg = pg.image.load('assets/sprites/dirtBlock.png').convert_alpha()
        self.fireImg = pg.image.load('assets/sprites/Fire0.png').convert_alpha()
        self.h2oImg = pg.image.load('assets/sprites/H2O.png').convert_alpha()
        self.totemImg = pg.image.load('assets/sprites/totems1.png').convert_alpha()

    def randomSeed(self, x, y):
        floors = np.zeros((y, x))
        for i in range(len(floors)):
            for j in range(len(floors[i])):
                if i > 2:
                    floors[i][j] = 1
        
        maskFire = np.zeros((y, x), dtype=bool)
        maskFire[3:, :] = True
        fireEntity = np.random.choice(np.flatnonzero(maskFire), size=self.level*7, replace=False)

        maskH2o = np.zeros((y, x), dtype=bool)
        maskH2o[4:, :] = True
        h2oEntity = np.random.choice(np.flatnonzero(maskH2o), size=self.level*3, replace=False)

        maskTotem = np.zeros((y, x), dtype=bool)
        maskTotem[4:, :] = True
        totemEntity = np.random.choice(np.flatnonzero(maskTotem), size=self.level*4, replace=False)

        floors.flat[fireEntity] = 2
        floors.flat[h2oEntity] = 3
        floors.flat[totemEntity] = 4
        floors[2][1] = 9
        return floors

    def printF(self):
        print(self.floors)

    def draw(self, surface):
        for i in range(len(self.floors)):
            for j in range(len(self.floors[i])):
                if self.floors[i][j] == 1:
                    dirtImg = pg.transform.scale(self.dirtImg, (self.dirtImg.get_width() * SPRITE_SCALE, self.dirtImg.get_height() * SPRITE_SCALE))
                    surface.blit(dirtImg, pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif self.floors[i][j] == 2:
                    fireImg = pg.transform.scale(self.fireImg, (self.fireImg.get_width() * SPRITE_SCALE, self.fireImg.get_height() * SPRITE_SCALE))
                    surface.blit(fireImg, pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif self.floors[i][j] == 3:
                    h2oImg = pg.transform.scale(self.h2oImg, (self.h2oImg.get_width() * SPRITE_SCALE, self.h2oImg.get_height() * SPRITE_SCALE))
                    surface.blit(h2oImg, pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif self.floors[i][j] == 4:
                    totemImg = pg.transform.scale(self.totemImg, (self.totemImg.get_width() * SPRITE_SCALE, self.totemImg.get_height() * SPRITE_SCALE))
                    surface.blit(totemImg, pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def getFloors(self):
        return self.floors