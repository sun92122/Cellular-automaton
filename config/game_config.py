from enum import Enum


class GameType(Enum):
    ConwaysGameOfLife = 1
    LangtonsAnt = 2
    BrianBrain = 3
    
    # return max number of game types
    @classmethod
    def max_num(cls):
        return max([e.value for e in cls])
    
    # return min number of game types
    @classmethod
    def min_num(cls):
        return min([e.value for e in cls])