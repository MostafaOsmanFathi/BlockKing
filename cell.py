from turtle import Turtle


class Cell(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shape("square")
        self.color("gray")
        self.penup()
        self.speed("fastest")
        self.goto(x, y)
        self.shapesize(stretch_wid=2, stretch_len=2)
