import numpy as np

from config import color_config as cc

"""
Brian's Brain
https://conwaylife.com/wiki/OCA:Brian%27s_Brain

每個細胞可能處於三種狀態之一：
開啟、死亡或關閉
每個細胞被認為有八個鄰居（Moore neighborhood）

細胞處於關閉狀態
但恰好有兩個鄰居處於打開狀態，則該細胞會打開

所有開啟的細胞都會進入死亡狀態

處於死亡狀態的細胞進入關閉狀態
"""

class BrianBrain(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.delay = 5
        self.grid = np.zeros((self.width, self.height), dtype=np.int8)
        self.next_grid = np.zeros((self.width, self.height), dtype=np.int8)
    
    def random_init(self):
        center_size = min(self.height, self.width) // 3
        center = np.random.randint(0, 3, (center_size, center_size)) % 2

        start_row = (self.height - center_size) // 2
        start_col = (self.width - center_size) // 2
        self.grid[start_col:start_col + center_size,
                  start_row:start_row + center_size] = center

    def update(self):
        for x in range(self.width):
            for y in range(self.height):
                self.next_grid[x][y] = self.get_next_state(x, y)
        self.grid = self.next_grid
    
    def get_next_state(self, x, y):
        if self.grid[x][y] == 0:
            if self.get_around(x, y):
                return 1
            else:
                return 0
        elif self.grid[x][y] == 1:
            return 2
        elif self.grid[x][y] == 2:
            return 0
    
    def get_around(self, x, y):
        around = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                if x + i < 0 or x + i >= self.width:
                    continue
                if y + j < 0 or y + j >= self.height:
                    continue
                if self.grid[x + i][y + j] == 1:
                    around += 1
        if around == 2:
            return True

    def get_color(self):
        # 0: black, 1: blue, 2: withe
        def color(x):
            if x == 0:
                return cc.BLACK
            elif x == 1:
                return cc.BLUE
            elif x == 2:
                return cc.WHITE

        return np.vectorize(color, otypes=[tuple])(self.grid)