import pygame as pg
from settings import *
import numpy as np

class Floor():
    def __init__(self, x, y, level):
        self.level = level
        self.floors = self.randomSeed(x, y)
        self.dirtImg = pg.image.load('assets/sprites/dirtBlock.png').convert_alpha()

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
                    pg.draw.rect(surface, (0,255,0), pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif self.floors[i][j] == 2:
                    pg.draw.rect(surface, (255,0,0), pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif self.floors[i][j] == 3:
                    pg.draw.rect(surface, (0,0,255), pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif self.floors[i][j] == 4:
                    pg.draw.rect(surface, (87,35,100), pg.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def getFloors(self):
        return self.floors