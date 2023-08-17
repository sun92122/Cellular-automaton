import numpy as np

import pygame as pg
from config import cell_config as cc
from config import layout_config as lc


class Screen(lc.Config):
    def __init__(self):
        super().__init__()
        self.screen = pg.display.set_mode(self.screen_size)
        self.show_grid = False
        self.monochrome = True
    
    def update(self, data: np.ndarray, col_max: int, row_max: int):
        self.screen.fill(self.bg_color)
        self.draw(data, col_max, row_max)
        pg.display.flip()
    
    def draw(self, data: np.ndarray, col_max: int, row_max: int):
        if self.show_grid:
            grid_color = np.vectorize(
                self.get_grid_color, otypes=[tuple]
                )(data)
        for x in np.arange(0, col_max):
            for y in np.arange(0, row_max):
                self.draw_block(data[x][y], x, y)
                self.draw_grid(grid_color[x][y], x, y)
    
    def draw_text(self, text: str, x: int, y: int):
        font = pg.font.SysFont(*self.font)
        text = font.render(text, True, cc.BLACK)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)
    
    def draw_block(self, color: tuple, x: int, y: int):
        pg.draw.rect(
            self.screen, color,
            pg.Rect(x * self.grid_size, y * self.grid_size,
                    self.grid_size, self.grid_size))
    
    def draw_grid(self, color: tuple, x: int, y: int, line_width: int = 1):
        # draw horizontal line left of the block
        if x:
            pg.draw.line(
                self.screen, color,
                (x * self.grid_size, y * self.grid_size),
                (x * self.grid_size, (y + 1) * self.grid_size),
                line_width)
        # draw vertical line below the block
        if y:
            pg.draw.line(
                self.screen, color,
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
