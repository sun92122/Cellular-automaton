class Config(object):
    def __init__(self):
        self.unit = 3
        self.line_width = 1
        self.grid_size = 2 * self.unit + self.line_width
        self.grid_col = 100
        self.grid_row = 100
        self.grid = (self.grid_col, self.grid_row)
        self.bg_color = (250, 250, 250)
        self._screen_right = 5
        self._screen_bottom = 5
        self.screen_size = (
            self.grid_col * self.grid_size + self._screen_right,
            self.grid_row * self.grid_size + self._screen_bottom)
        self.font = ('Comic Sans MS', int(100 * (self.unit / 10)**1.5))