from turtle import Screen, Turtle
from cell import Cell
from map import Map
from CONSTANTS import *


def main():
    mp = Map()
    mp.draw_grid(N_CELLS, M_CELLS)
    mp.screen.update()
    mp.screen.mainloop()


if __name__ == '__main__':
    main()
