from config import color_config as cc

class Config(object):
    def __init__(self):
        self.unit = 2

        self.line_width = 1
        self.padding = 5

        self.grid_size = 2 * self.unit + self.line_width
        self.grid_col = 150
        self.grid_row = 150
        self.grid = (self.grid_col, self.grid_row)

        self.game_canva_size = (
            self.grid_col * self.grid_size,
            self.grid_row * self.grid_size)
        self.game_canva_width, self.game_canva_height = self.game_canva_size
        self.game_canva_location = (self.padding, self.padding)

        self.side_canva_size = (
            400, self.game_canva_height)
        self.side_canva_width, self.side_canva_height = self.side_canva_size
        self.side_canva_location = (
            self.game_canva_width + self.padding * 2, self.padding)

        self.bg_color = cc.WHITE_SMOKE
        self.screen_size = (
            self.game_canva_width + self.side_canva_width + self.padding * 3,
            self.game_canva_height + self.padding * 2)
        self.screen_width, self.screen_height = self.screen_size

        self.font = ('Comic Sans MS', 20)