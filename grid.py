import os.path
import sys
from turtle import Screen

from CONSTANTS import *
from cell import Cell
from textures import Textures


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Grid:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("BlockKing")
        self.screen.tracer(0)
        self.grid = []
        img_folder = resource_path("img")
        if os.path.exists(img_folder):
            for file in os.listdir(img_folder):
                if file.endswith(".gif") or file.endswith(".png"):
                    img_path = os.path.join(img_folder, file)
                    if img_path.find('\\') != -1:
                        Textures.color_dict['img/' + img_path.split('\\')[-1]] = img_path
                    else:
                        Textures.color_dict[img_path.split('/')[-1]] = img_path

                    if file.endswith(".gif"):
                        self.screen.addshape(img_path)
                    print(img_path)

        self.screen.bgpic(Textures.color_dict['img/bg.png'])

    def draw_grid(self, n, m):
        x, y = START_X, START_Y
        for i in range(n):
            self.grid.append([])
            for j in range(m):
                self.grid[-1].append(Cell(x, y))
                x += (SQUARE_SIZE + FIXED_MARGIN)
            y += -(SQUARE_SIZE + FIXED_MARGIN)
            x = START_X
