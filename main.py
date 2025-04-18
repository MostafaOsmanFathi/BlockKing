from time import sleep
from turtle import Screen, Turtle
from cell import Cell
from grid import Grid
from CONSTANTS import *
from player import Player


def main():
    mp = Grid()
    mp.draw_grid(N_CELLS, M_CELLS)
    player = Player('green', mp, 0, 0)
    mp.screen.listen()

    while True:
        mp.screen.update()
        sleep(0.1)
    # mp.screen.exitonclick()
    mp.screen.mainloop()


if __name__ == '__main__':
    main()
