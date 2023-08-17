import pygame as pg
from config import layout_config as lc
from config import cell_config as cc
from config.game_config import GameType
from layout.screen import Screen
from rule.conway_gol import ConwaysGameOfLife
from rule.langton_ant import LangtonsAnt

class Game(object):
    def __init__(self):
        pg.init()
        self.screen = Screen()
        self.layout = lc.Config()

        self.clock = pg.time.Clock()

        self.choossing = True
        self.running = True
        self.update_counter = 1
        self.pause = False
        self.game_type = None
        self.game_type_chosen = None

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
            self.screen.update(
                [], self.layout.grid_col, self.layout.grid_row)

            if GameType.ConwaysGameOfLife == self.game_type:
                pg.display.set_caption("Conway's Game of Life")
                self.game = ConwaysGameOfLife(
                    self.layout.grid_col, self.layout.grid_row)
                self.game.random_init()
                self.choossing = False
            elif GameType.LangtonsAnt == self.game_type:
                pg.display.set_caption("Langton's Ant")
                self.game = LangtonsAnt(
                    self.layout.grid_col, self.layout.grid_row)
                # self.game.random_init()
                self.choossing = False

            self.clock.tick_busy_loop(60)

    def game_loop(self):
        while self.running:
            # Event handling
            self.event_handler()

            # update
            if self.update_counter % self.game.delay == 0 and not self.pause:
                self.game.update()
                self.update_counter = 1
            else:
                self.update_counter += 1
            # draw
            self.update()
            self.custom_draw()

            self.clock.tick_busy_loop(60)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.game.update()
                    self.update_counter = 1
            if event.type == pg.QUIT:
                self.running = False

    def choose_event_handler(self, choose):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.game_type = GameType.ConwaysGameOfLife
                if event.key == pg.K_2:
                    self.game_type = GameType.LangtonsAnt
                if (event.key == pg.K_KP_ENTER or
                    event.key == pg.K_RETURN):
                    self.game_type = self.game_type_chosen
                    self.choossing = False
                if event.key == pg.K_ESCAPE:
                    self.choossing = False
                    self.running = False
            if event.type == pg.QUIT:
                self.choossing = False
                self.running = False

    def update(self):
        self.screen.update(
            self.game.get_color(),
            self.game.width, self.game.height)

    def custom_draw(self):
        if GameType.LangtonsAnt == self.game_type:
            pg.draw.polygon(
                self.screen.screen, cc.RED,
                self.game.ant_location(self.layout.grid_size))
