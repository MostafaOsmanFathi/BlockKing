from turtle import Turtle


class TurtleCamera(Turtle):
    lst_of_objects = []
    last_x = 0
    last_y = 0

    def __init__(self):
        super().__init__()
        TurtleCamera.lst_of_objects.append(self)

    @classmethod
    def reset(cls):
        for obj in cls.lst_of_objects:
            obj.goto(obj.xcor() - cls.last_x, obj.ycor() - cls.last_y)
        cls.last_x = 0
        cls.last_y = 0

    @classmethod
    def change_camera(cls, x, y):
        for obj in cls.lst_of_objects:
            obj.goto(obj.xcor() + x - cls.last_x, obj.ycor() + y - cls.last_y)

        cls.last_x = x
        cls.last_y = y
