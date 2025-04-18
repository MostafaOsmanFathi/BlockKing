from turtle import Screen, Turtle
from cell import Cell
from grid import Grid
from CONSTANTS import *
from player import Player


def main():
    mp = Grid()
    mp.draw_grid(N_CELLS, M_CELLS)
    mp.screen.update()
    player = Player('green', mp, 0, 0)
    player.set_dir_right()
    player.move()
    mp.screen.update()
    # mp.screen.exitonclick()
    mp.screen.mainloop()


if __name__ == '__main__':
    main()
