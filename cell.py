import player
from CONSTANTS import *
from turtle_camera import TurtleCamera


class Cell(TurtleCamera):
    def __init__(self, x, y):
        super().__init__()
        # self.shape("square")
        self.shape("img/def_block.gif")
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
            # self.change_color(f'img/light_{player.player_color}.gif')
            self.shape(f'img/light_{player.player_color}.gif')

    def set_full_owner(self, player: player.Player):
        self.cell_full_owner = player
        self.cell_temp_owner = None
        # self.change_color(f'img/dark_{player.player_color}.gif')
        self.shape(f'img/dark_{player.player_color}.gif')
