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

    def set_owner(self, owner: player.Player):
        if self.cell_temp_owner == owner:
            self.cell_full_owner = owner
            self.change_color('dark' + owner.player_color)
        else:
            self.cell_temp_owner = owner
            self.change_color('light' + owner.player_color)

    def set_full_owner(self, owner: player.Player):
        self.cell_full_owner = owner
        self.change_color('dark' + owner.player_color)
