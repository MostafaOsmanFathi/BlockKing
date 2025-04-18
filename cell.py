from turtle import Turtle
from CONSTANTS import *


class Cell(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(SQUARE_COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(x, y)
        self.shapesize(stretch_wid=SQUARE_SCALE, stretch_len=SQUARE_SCALE)

    def change_color(self, color):
        self.color(color)