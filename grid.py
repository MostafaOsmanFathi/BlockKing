import os.path
from turtle import Screen

from CONSTANTS import *
from cell import Cell


class Grid:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("BlockKing")
        self.screen.tracer(0)
        self.screen.bgpic('img/bg.png')
        self.grid = []
        if os.path.exists('img'):
            for file in os.listdir('img'):
                if file.endswith('.gif'):
                    self.screen.addshape('img/' + file)
                    print('img/' + file)

    def draw_grid(self, n, m):
        x, y = START_X, START_Y
        for i in range(n):
            self.grid.append([])
            for j in range(m):
                self.grid[-1].append(Cell(x, y))
                x += (SQUARE_SIZE + FIXED_MARGIN)
            y += -(SQUARE_SIZE + FIXED_MARGIN)
            x = START_X
