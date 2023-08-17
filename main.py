import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

from core.game import Game

DEBUG = False

def main():
    game = Game()
    game.run()
    print('bye~')

if __name__ == '__main__':
    main()