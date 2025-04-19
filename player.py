from turtle import Turtle
from CONSTANTS import *
from time import sleep


class Player(Turtle):
    def __init__(self, color, grid, x, y, keyboard_set):
        super().__init__()
        self.x_cell_poss = x
        self.y_cell_poss = y
        self.shape("square")
        self.color(color)
        self.player_color = color
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=PLAYER_SCALE, stretch_len=PLAYER_SCALE)
        self.grid = grid
        self.goto(grid.grid[x][y].xcor(), grid.grid[x][y].ycor())

        # Set spawn position (initial position)
        self.spawn_position = (grid.grid[x][y].xcor(), grid.grid[x][y].ycor())

        # Add kill counter
        self.kills = 0
        self.deaths = 0

        self.dir = 0
        self.start_moving = False
        self.list_of_cells = []
        self.trail_cells = []
        self.claimed_cells = []

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
        if self.dir != 2 or not self.start_moving:
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
        if not self.can_move():
            return

        self.x_cell_poss += PLAYER_MOVEMENTS[self.dir][0]
        self.y_cell_poss += PLAYER_MOVEMENTS[self.dir][1]
        x = self.grid.grid[self.x_cell_poss][self.y_cell_poss].xcor()
        y = self.grid.grid[self.x_cell_poss][self.y_cell_poss].ycor()
        self.goto(x, y)
        self.list_of_cells.append((self.x_cell_poss, self.y_cell_poss))

    def fill_cells(self):
        for x, y in self.list_of_cells:
            self.grid.grid[x][y].set_full_owner(self)
        self.list_of_cells.clear()

    def clear_trail(self):
        for x, y in self.trail_cells:
            self.grid.grid[x][y].clear_temp_owner()
        self.trail_cells.clear()

    def reset_position(self):
        # Flash player when killed
        self.color('white')
        self.grid.screen.update()
        sleep(0.1)
        self.color(self.player_color)
        self.grid.screen.update()

        # Return to spawn position
        self.goto(self.spawn_position)
        # Reset position on grid
        self.x_cell_poss = self.grid.get_cell_index_by_coord(self.spawn_position[0])[0]
        self.y_cell_poss = self.grid.get_cell_index_by_coord(self.spawn_position[1])[1]
        # Clear trail and claimed cells
        self.clear_trail()
        self.claimed_cells.clear()
        self.trail_cells.clear()
        self.list_of_cells.clear()
        self.start_moving = False
        self.deaths += 1