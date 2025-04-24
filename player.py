from CONSTANTS import *
from turtle_camera import TurtleCamera


class Player(TurtleCamera):
    def __init__(self, color, grid, x, y, keyboard_set):
        super().__init__()
        self.x_cell_poss = x
        self.y_cell_poss = y
        # self.shape("square")
        self.shape(f'img/{color}.gif')
        self.player_color = color
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=PLAYER_SCALE, stretch_len=PLAYER_SCALE)
        self.goto(grid.grid[x][y].xcor(), grid.grid[x][y].ycor())
        self.dir = 0
        self.grid = grid
        self.start_moving = False
        self.list_of_cells = []

        if keyboard_set == 1:
            grid.screen.onkey(lambda: self.set_dir_right(), "d")
            grid.screen.onkey(lambda: self.set_dir_left(), "a")
            grid.screen.onkey(lambda: self.set_dir_up(), "w")
            grid.screen.onkey(lambda: self.set_dir_down(), "s")
        else:
            grid.screen.onkey(lambda: self.set_dir_right(), "Right")
            grid.screen.onkey(lambda: self.set_dir_left(), "Left")
            grid.screen.onkey(lambda: self.set_dir_up(), "Up")
            grid.screen.onkey(lambda: self.set_dir_down(), "Down")

    def set_dir_up(self):
        if self.dir != 2 or (not self.start_moving):
            self.dir = 3
            self.start_moving = True

    def set_dir_down(self):
        if self.dir != 3 or not self.start_moving:
            self.dir = 2
            self.start_moving = True

    def set_dir_left(self):
        if self.dir != 0 or not self.start_moving:
            self.dir = 1
            self.start_moving = True

    def set_dir_right(self):
        if self.dir != 1 or not self.start_moving:
            self.dir = 0
            self.start_moving = True

    def can_move(self):
        new_x = self.x_cell_poss + PLAYER_MOVEMENTS[self.dir][0]
        new_y = self.y_cell_poss + PLAYER_MOVEMENTS[self.dir][1]
        return 0 <= new_x < N_CELLS and 0 <= new_y < M_CELLS

    def move(self):
        self.start_moving = True
        self.x_cell_poss += PLAYER_MOVEMENTS[self.dir][0]
        self.y_cell_poss += PLAYER_MOVEMENTS[self.dir][1]
        if self.can_move():
            x = self.grid.grid[self.x_cell_poss][self.y_cell_poss].xcor()
            y = self.grid.grid[self.x_cell_poss][self.y_cell_poss].ycor()
            self.goto(x, y)
            if self.grid.grid[self.x_cell_poss][self.y_cell_poss].cell_full_owner != self:
                self.list_of_cells.append((self.x_cell_poss, self.y_cell_poss))

    def fill_cells(self):
        for x, y in self.list_of_cells:
            self.grid.grid[x][y].set_full_owner(self)
        self.list_of_cells.clear()
