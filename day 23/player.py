from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.speed(0)
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.speed(1)
        self.level = 1

    def check_if_win(self):
        if self.ycor() > FINISH_LINE_Y:
            self.level += 1
            return True

        else:
            return False

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def die_check(self, car_list):
        for car in car_list:
            current_y = abs(car.ycor())
            result = current_y - abs(self.ycor())
            if -20 < result < 20 and self.distance(car) < 29:
                print("rip")
                return True
            else:
                pass

    def win_check(self):
        current_y = self.ycor()

        if current_y >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

