from turtle_camera import TurtleCamera


class Camera:
    def __init__(self, object_to_focus: TurtleCamera = None):
        self.object_to_focus = object_to_focus

    def get_cors(self):
        if self.object_to_focus is None:
            return 0, 0
        return self.object_to_focus.xcor(), self.object_to_focus.ycor()

    def get_xcor(self):
        if self.object_to_focus is None:
            return 0
        return self.object_to_focus.xcor()

    def get_ycor(self):
        if self.object_to_focus is None:
            return 0
        return self.object_to_focus.xcor()

    def get_neg_cors(self):
        if self.object_to_focus is None:
            return 0, 0
        return -self.object_to_focus.xcor(), -self.object_to_focus.ycor()

    def get_neg_xcor(self):
        if self.object_to_focus is None:
            return 0
        return -self.object_to_focus.xcor()

    def get_neg_ycor(self):
        if self.object_to_focus is None:
            return 0
        return -self.object_to_focus.xcor()
