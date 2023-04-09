from settings import *
import pygame as pg
import pygame.freetype as ft
import sys

class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.clock = pg.time.Clock()
        self.font = ft.SysFont('Verdana', FONT_SIZE)
        self.dt = 0.0

    def update(self):
        pg.display.flip()
        self.dt = self.clock.tick() * 0.001

    def draw(self):
        self.screen.fill('black')
        self.draw_fps()

    def draw_fps(self):
        fps = f'{self.clock.get_fps() :.0f} FPS'
        self.font.render_to(self.screen, (0,0), text=fps, fgcolor='white', bgcolor='black')

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()