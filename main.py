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
        self.load_modules()
        self.start_time = 0
        self.game_over = False
        self.menu = True

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if self.menu:
                    self.menu = False
                    self.start_time = pg.time.get_ticks()
                else:
                    self.player.check_events(event)

    def load_modules(self):
        self.player = Player()
        self.floor = Floor(19, 13, 1)

    def update(self):
        if not self.menu:
            self.player.update(self.floor.getFloors())

    def draw_fps(self):
        fps = f'{self.clock.get_fps():.0f} FPS'
        fps_surface, fps_rect = self.font.render(fps, fgcolor='white', bgcolor='black')
        fps_pos = (10, 10)
        self.screen.blit(fps_surface, fps_pos)

    def draw_timer(self):
        elapsed_time = (pg.time.get_ticks() - self.start_time) // 1000
        remaining_time = max(0, 120 - elapsed_time)
        time_str = f'Time: {remaining_time}s'
        time_surface, time_rect = self.font.render(time_str, fgcolor='white', bgcolor='black')
        time_pos = (self.screen.get_width() - time_rect.width - 10, 10)
        self.screen.blit(time_surface, time_pos)

    def draw_menu(self):
        self.screen.fill('black')
        title_str = 'Forbidden Treasures PyGame'
        title_surface, title_rect = self.font.render(title_str, fgcolor='white', bgcolor='black')
        title_pos = ((self.screen.get_width() - title_rect.width) // 2, 100)
        self.screen.blit(title_surface, title_pos)
        start_str = 'Press any key to start'
        start_surface, start_rect = self.font.render(start_str, fgcolor='white', bgcolor='black')
        start_pos = ((self.screen.get_width() - start_rect.width) // 2, 300)
        self.screen.blit(start_surface, start_pos)
        pg.display.flip()

    def draw(self):
        if self.menu:
            self.draw_menu()
        else:
            self.screen.fill('black')
            self.player.draw(self.screen)
            self.floor.draw(self.screen)
            self.draw_fps()
            self.draw_timer()
            pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(60)

            elapsed_time = (pg.time.get_ticks() - self.start_time) // 1000
            if elapsed_time >= 120:
                self.game_over = True

            if self.game_over:
                self.game_over_screen()
                break 

    def game_over_screen(self):
        game_over_image = pg.image.load('assets/sprites/playerMuerte.png').convert_alpha()
        game_over_rect = game_over_image.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(game_over_image, game_over_rect)
        pg.display.flip()
        pg.time.wait(3000)  # Esperar 3 segundos antes de salir
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = App()
    app.run()
