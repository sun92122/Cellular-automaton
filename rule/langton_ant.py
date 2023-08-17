import numpy as np

from config import cell_config as cc

"""
Langton's ant

在平面上的正方形格被填上黑色或白色
在其中一格正方形有一隻「螞蟻」，它的頭部朝向上下左右其中一方

若螞蟻在白格，右轉90度，將該格改為黑格，向前移一步
若螞蟻在黑格，左轉90度，將該格改為白格，向前移一步
"""

class LangtonsAnt(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.delay = 5
        self.grid = np.empty((self.width, self.height), dtype=tuple)
        self.grid.fill(cc.WHITE)
        self.ant_x = self.width // 2
        self.ant_y = self.height // 2
        self.ant_dir = np.choose(np.random.randint(4),
                                 [[0, 1], [1, 0], [0, -1], [-1, 0]])

    def random_init(self):
        self.grid = np.random.randint(
            2, size=(self.width, self.height), dtype=np.int8)

    def update(self):
        if self.grid[self.ant_x][self.ant_y] == cc.WHITE:
            self.ant_dir = np.array([-self.ant_dir[1], self.ant_dir[0]])
            self.grid[self.ant_x][self.ant_y] = cc.BLACK
        else:
            self.ant_dir = np.array([self.ant_dir[1], -self.ant_dir[0]])
            self.grid[self.ant_x][self.ant_y] = cc.WHITE
        self.ant_x += self.ant_dir[0]
        self.ant_y += self.ant_dir[1]

    def get_color(self):
        return np.vectorize(
            lambda x: cc.BLACK if x == 1 else cc.WHITE, otypes=[tuple]
            )(self.grid)
    
    def ant_location(self, grid_size):
        ant_mid = np.array([self.ant_x, self.ant_y]) + 0.5
        return np.array([
            ant_mid + self.ant_dir * 0.3,
            ant_mid - self.ant_dir * 0.2 + np.array([-self.ant_dir[1], self.ant_dir[0]]) * 0.3,
            ant_mid - self.ant_dir * 0.2 - np.array([-self.ant_dir[1], self.ant_dir[0]]) * 0.3
        ]) * grid_size