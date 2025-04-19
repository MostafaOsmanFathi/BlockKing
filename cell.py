from turtle import Turtle

import player
from CONSTANTS import *


class Cell(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(SQUARE_COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(x, y)
        self.shapesize(stretch_wid=SQUARE_SCALE, stretch_len=SQUARE_SCALE)
        self.cell_full_owner = None
        self.cell_temp_owner = None

    def change_color(self, color):
        self.color(color)

    def set_temp_owner(self, player: player.Player):
        if self.cell_full_owner != player:
            self.cell_temp_owner = player
            self.cell_full_owner = None
            self.change_color('light' + player.player_color)

    def set_full_owner(self, player: player.Player):
        self.cell_full_owner = player
        self.cell_temp_owner = None
        self.change_color('dark' + player.player_color)
