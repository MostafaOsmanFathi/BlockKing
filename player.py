from turtle import Turtle
from CONSTANTS import *


class Player(Turtle):
    def __init__(self, color, grid, x, y):
        super().__init__()
        self.x_cell_poss = x
        self.y_cell_poss = y
        self.shape("square")
        self.color(color)
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=PLAYER_SCALE, stretch_len=PLAYER_SCALE)
        self.goto(grid.grid[x][y].xcor(), grid.grid[x][y].ycor())
        self.dir = 0
        self.grid = grid

    def set_dir_up(self):
        self.dir = 3

    def set_dir_down(self):
        self.dir = 2

    def set_dir_left(self):
        self.dir = 1

    def set_dir_right(self):
        self.dir = 0

    def move(self):
        self.x_cell_poss += PLAYER_MOVEMENTS[self.dir][0]
        self.y_cell_poss += PLAYER_MOVEMENTS[self.dir][1]
        self.x_cell_poss = min(self.x_cell_poss, N_CELLS - 1)
        self.x_cell_poss = max(self.x_cell_poss, 0)
        self.y_cell_poss = min(self.y_cell_poss, M_CELLS - 1)
        self.y_cell_poss = max(self.y_cell_poss, 0)
        x = self.grid.grid[self.x_cell_poss][self.y_cell_poss].xcor()
        y = self.grid.grid[self.x_cell_poss][self.y_cell_poss].ycor()
        print("new poss", x, y)
        self.goto(x, y)
