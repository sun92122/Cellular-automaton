import time
import pygame as pg
from config import layout_config as lc
from config import color_config as cc
from config.game_config import GameType
from layout.screen import Screen

from rule.conway_gol import ConwaysGameOfLife
from rule.langton_ant import LangtonsAnt
from rule.brian_brain import BrianBrain

class Game(object):
    def __init__(self):
        pg.init()
        self.screen = Screen()

        self.clock = pg.time.Clock()

        self.choossing = True
        self.running = True
        self.update_counter = 1
        self.pause = False
        self.game_type = None
        self.game_type_chosen_num = 1
        self.step = 0

    def run(self):
        self.choossing_loop()
        if self.game_type is not None:
            self.game_loop()
        pg.quit()

    def choossing_loop(self):
        while self.choossing:
            # Event handling
            self.choose_event_handler()

            # choose game type show
            self.screen.side_canva_fill(self.screen.bg_color)
            self.screen.draw_text_left(
                "1. Conway's Game of Life", 10, 100)
            self.screen.draw_text_left(
                "2. Langton's Ant", 10, 150)
            self.screen.draw_text_left(
                "3. Brian's Brain", 10, 200)
            self.screen.draw_text_center(
                f"choose: {self.game_type_chosen_num}",
                self.screen.side_canva_width / 2, 250)
            self.screen.draw_text_center(
                "up/down to choose, ENTER to confirm", 
                self.screen.side_canva_width / 2, 300)
            self.screen.draw_text_center(
                "ESC to exit",
                self.screen.side_canva_width / 2, 350)
            self.screen.update()

            if GameType.ConwaysGameOfLife == self.game_type:
                pg.display.set_caption("Conway's Game of Life")
                self.game = ConwaysGameOfLife(
                    self.screen.grid_col, self.screen.grid_row)
                self.game.random_init()
                self.choossing = False
            elif GameType.LangtonsAnt == self.game_type:
                pg.display.set_caption("Langton's Ant")
                self.game = LangtonsAnt(
                    self.screen.grid_col, self.screen.grid_row)
                # self.game.random_init()
                self.screen.show_grid = True
                self.choossing = False
            elif GameType.BrianBrain == self.game_type:
                pg.display.set_caption("Brian's Brain")
                self.game = BrianBrain(
                    self.screen.grid_col, self.screen.grid_row)
                self.game.random_init()
                self.choossing = False

            self.clock.tick_busy_loop(30)

    def game_loop(self):
        while self.running:
            # Event handling
            self.event_handler()

            # update
            if self.update_counter % self.game.delay == 0 and not self.pause:
                self.game.update()
                self.step += 1
                self.update_counter = 1
            else:
                self.update_counter += 1
            # draw
            self.screen.fill()
            self.draw()
            self.custom_draw()
            self.screen.update()

            self.clock.tick_busy_loop(60)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.game.update()
                    self.step += 1
                    self.update_counter = 1
                # space to pause
                if event.key == pg.K_SPACE:
                    self.pause = not self.pause
                # g to show grid
                if event.key == pg.K_g:
                    self.screen.show_grid = not self.screen.show_grid
                if event.key == pg.K_ESCAPE:
                    self.running = False

            if event.type == pg.QUIT:
                self.running = False

    def choose_event_handler(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1 or event.key == pg.K_KP1:
                    self.game_type = GameType.ConwaysGameOfLife
                if event.key == pg.K_2 or event.key == pg.K_KP2:
                    self.game_type = GameType.LangtonsAnt
                if event.key == pg.K_3 or event.key == pg.K_KP3:
                    self.game_type = GameType.BrianBrain
                if event.key == pg.K_UP:
                    self.game_type_chosen_num = max(
                        GameType.min_num(), self.game_type_chosen_num - 1)
                if event.key == pg.K_DOWN:
                    self.game_type_chosen_num = min(
                        GameType.max_num(), self.game_type_chosen_num + 1)
                if (event.key == pg.K_KP_ENTER or
                    event.key == pg.K_RETURN):
                    self.game_type = GameType(self.game_type_chosen_num)
                    self.choossing = False
                if event.key == pg.K_ESCAPE:
                    self.choossing = False
                    self.running = False
            if event.type == pg.QUIT:
                self.choossing = False
                self.running = False

    def draw(self):
        self.screen.draw(
            self.game.get_color(),
            self.game.width, self.game.height)
        self.screen.draw_text_left(
            f"step: {self.step}", 10, 10)

    def custom_draw(self):
        if GameType.LangtonsAnt == self.game_type:
            self.screen.draw_polygon(
                cc.RED, self.game.ant_location(self.screen.grid_size))
