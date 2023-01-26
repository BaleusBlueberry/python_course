from turtle import Turtle


class Pong(Turtle):

    def __init__(self, x_cods, y_cords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.goto(x_cods, y_cords)

    def move_up(self):
        if self.ycor() > 240:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() < -240:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


