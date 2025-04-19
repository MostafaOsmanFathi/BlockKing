from turtle import Turtle, Screen

from cell import Cell

from CONSTANTS import *


class Grid:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("BlockKing")
        self.screen.tracer(0)
        self.grid = []

    def draw_grid(self, n, m):
        x, y = START_X, START_Y
        for i in range(n):
            self.grid.append([])
            for j in range(m):
                self.grid[-1].append(Cell(x, y))
                x += (SQUARE_SIZE + FIXED_MARGIN)
            y += -(SQUARE_SIZE + FIXED_MARGIN)
            x = START_X

    def get_cell_index_by_coord(self, coord):
        # Calculate which cell contains the given coordinate
        start_x = START_X
        start_y = START_Y
        cell_size = SQUARE_SIZE + FIXED_MARGIN

        # For x coordinate
        x_index = int((coord - start_x) // cell_size)

        # For y coordinate (since y decreases as we go down rows)
        y_index = int((start_y - coord) // cell_size)

        return x_index, y_index