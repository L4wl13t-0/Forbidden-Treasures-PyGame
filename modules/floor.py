import pygame as pg
from settings import *

class Floor():
    def __init__(self):
        self.floors = [pg.Rect(0, 144, TILE_SIZE, TILE_SIZE),
                       pg.Rect(0, 192, TILE_SIZE, TILE_SIZE),
                       pg.Rect(0, 240, TILE_SIZE, TILE_SIZE),
                       pg.Rect(0, 288, TILE_SIZE, TILE_SIZE),
                       pg.Rect(0, 336, TILE_SIZE, TILE_SIZE),
                       pg.Rect(0, 384, TILE_SIZE, TILE_SIZE),
                       pg.Rect(0, 432, TILE_SIZE, TILE_SIZE),
                       pg.Rect(0, 480, TILE_SIZE, TILE_SIZE),
                       pg.Rect(48, 528, TILE_SIZE, TILE_SIZE),
                       pg.Rect(96, 528, TILE_SIZE, TILE_SIZE)]

    def draw(self, surface):
        for floor in self.floors:
            pg.draw.rect(surface, (0,0,255), floor)

    def getFloors(self):
        return self.floors