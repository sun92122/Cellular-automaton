import numpy as np

from config import cell_config as cc

"""
Conway's Game of Life

每個細胞有兩種狀態 - 存活或死亡
每個細胞與以自身為中心的周圍八格細胞產生互動

當前細胞為存活狀態時
當周圍的存活細胞低於2個時（不包含2個），該細胞變成死亡狀態 underpopulation
當周圍有2個或3個存活細胞時，該細胞保持原樣
當周圍有超過3個存活細胞時，該細胞變成死亡狀態 overpopulation

當前細胞為死亡狀態時
當周圍有3個存活細胞時，該細胞變成存活狀態 reproduction
"""

class ConwaysGameOfLife(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.delay = 5
        self.grid = np.zeros((self.width, self.height), dtype=np.int8)
        self.next_grid = np.zeros((self.width, self.height), dtype=np.int8)
        self.around = np.zeros((self.width, self.height), dtype=np.int8)
    
    def random_init(self):
        self.grid = np.random.randint(2, size=(self.width, self.height), dtype=np.int8)
        for x in range(self.width):
            for y in range(self.height):
                self.around[x][y] = self.get_around(x, y)

    def update(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = self.get_next_state(x, y)
        for x in range(self.width):
            for y in range(self.height):
                self.around[x][y] = self.get_around(x, y)
    
    def get_next_state(self, x, y):
        around = self.around[x][y]
        if self.grid[x][y] == 1:
            if around < 2:                      # underpopulation
                return 0
            elif around == 2 or around == 3:    # keep alive
                return 1
            elif around > 3:                    # overpopulation
                return 0
        else:
            if around == 3:                     # reproduction
                return 1
            else:                               # keep dead
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
                around += self.grid[x + i][y + j]
        return around

    def get_color(self):
        return np.vectorize(
            lambda x: cc.BLACK if x == 1 else cc.WHITE, otypes=[tuple]
            )(self.grid)