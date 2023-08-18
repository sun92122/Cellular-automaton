import numpy as np

import pygame as pg
from pygame import locals
from config import color_config as cc
from config import layout_config as lc


class Screen(lc.Config):
    def __init__(self):
        super().__init__()
        flags = locals.DOUBLEBUF
        self.screen = pg.display.set_mode(self.screen_size, flags)

        self.game_canva = pg.Surface(self.game_canva_size)
        self.game_canva = self.game_canva.convert()
        
        self.side_canva = pg.Surface(self.side_canva_size)
        self.side_canva = self.side_canva.convert()
        
        self.show_grid = False
        self.monochrome = True
        self.font = pg.font.SysFont(*self.font)

    def fill(self, color: tuple = ()):
        if not color:
            color = self.bg_color
        self.game_canva_fill(color)
        self.side_canva_fill(color)

    def screen_fill(self, color: tuple):
        self.screen.fill(color)

    def game_canva_fill(self, color: tuple):
        self.game_canva.fill(color)

    def side_canva_fill(self, color: tuple):
        self.side_canva.fill(color)
    
    def update(self):
        self.update_game()
        self.update_side()
    
    def update_game(self):
        self.screen.blit(self.game_canva, self.game_canva_location)
        pg.display.update(
            self.game_canva_location + self.game_canva_size)
        
    def update_side(self):
        self.screen.blit(self.side_canva, self.side_canva_location)
        pg.display.update(
            self.side_canva_location + self.side_canva_size)
    
    def draw(self, data: np.ndarray, col_max: int, row_max: int):
        self.game_canva_fill(self.bg_color)
        self.draw_game(data, col_max, row_max)
    
    def draw_game(self, data: np.ndarray, col_max: int, row_max: int):
        if self.show_grid:
            grid_color = np.vectorize(
                self.get_grid_color, otypes=[tuple]
                )(data)
        for x in np.arange(0, col_max):
            for y in np.arange(0, row_max):
                self.draw_block(data[x][y], x, y)
                if self.show_grid:
                    self.draw_grid(grid_color[x][y], x, y)
    
    def draw_text(self, text: str, x: int, y: int):
        self.draw_text_center(text, x, y)
    
    def draw_text_center(self, text: str, x: int, y: int):
        text = self.font.render(text, True, cc.BLACK)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.side_canva.blit(text, text_rect)
    
    def draw_text_left(self, text: str, x: int, y: int):
        text = self.font.render(text, True, cc.BLACK)
        text_rect = text.get_rect()
        text_rect.topleft = (x, y)
        self.side_canva.blit(text, text_rect)
    
    def draw_text_right(self, text: str, x: int, y: int):
        text = self.font.render(text, True, cc.BLACK)
        text_rect = text.get_rect()
        text_rect.topright = (x, y)
        self.side_canva.blit(text, text_rect)
    
    def draw_polygon(self, color: tuple, points: list):
        pg.draw.polygon(self.game_canva, color, points)
    
    def draw_block(self, color: tuple, x: int, y: int):
        pg.draw.rect(
            self.game_canva, color,
            pg.Rect(x * self.grid_size, y * self.grid_size,
                    self.grid_size, self.grid_size))
    
    def draw_grid(self, color: tuple, x: int, y: int, line_width: int = 1):
        # draw horizontal line left of the block
        if x:
            pg.draw.line(
                self.game_canva, color,
                (x * self.grid_size, y * self.grid_size),
                (x * self.grid_size, (y + 1) * self.grid_size),
                line_width)
        # draw vertical line below the block
        if y:
            pg.draw.line(
                self.game_canva, color,
                (x * self.grid_size, y * self.grid_size),
                ((x + 1) * self.grid_size, y * self.grid_size),
                line_width)

    def get_grid_color(self, color: tuple):
        if self.monochrome:
            return cc.LIGHT_GRAY
        return cc.BLACK if self.brightness(color) > 127 else cc.WHITE

    def brightness(self, color: tuple):
        if self.monochrome:
            return (color[0] + color[1] + color[2]) / 3
        return 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]
