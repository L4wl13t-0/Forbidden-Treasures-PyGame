from settings import *
import pygame as pg
import pygame.freetype as ft
from modules.player import Player
from modules.floor import Floor
import sys

class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.clock = pg.time.Clock()
        self.font = ft.SysFont('Verdana', FONT_SIZE)
        pg.display.set_caption('Forbidden Treasures PyGame')
        self.dt = 0.0
        self.load_modules()

    def load_modules(self):
        self.player = Player()
        self.floor = Floor()

    def update(self):
        pg.display.flip()
        self.player.update(self.dt, self.floor.getFloors())
        self.dt = self.clock.tick(60) / 1000.0

    def draw(self):
        self.screen.fill('black')
        self.draw_fps()
        self.player.draw(self.screen)
        self.floor.draw(self.screen)

    def draw_fps(self):
        fps = f'{self.clock.get_fps() :.0f} FPS'
        self.font.render_to(self.screen, (0,0), text=fps, fgcolor='white', bgcolor='black')

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            self.player.check_events(e)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()