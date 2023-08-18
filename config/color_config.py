# color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# white
WHITE = (255, 255, 255)
WHITE_SMOKE = (245, 245, 245)
# gray
LIGHT_GRAY = (211, 211, 211)
SLIVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

class Config(object):
    def __init__(self):
        self.COLOR_DEAD = BLACK
        self.COLOR_ALIVE = WHITE