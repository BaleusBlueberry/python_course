from turtle import Turtle


vertical_move = {
    "up": 10,
    "down": -10,
}

horizontal_move = {
    "right": 10,
    "left": -10,
}
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("White")
        self.speed(2)
        self.horizontal_direction = "right"
        self.vertical_direction = "up"


    def move(self):
        new_y = self.ycor() + vertical_move[self.vertical_direction]
        new_x = self.xcor() + horizontal_move[self.horizontal_direction]
        self.goto(new_x, new_y)


    def detect_wall_collision(self):
        y_cords = abs(self.ycor())

        if y_cords > 280:
            if self.vertical_direction == "up":
                self.vertical_direction = "down"
            else:
                self.vertical_direction = "up"

    def detect_player_collision(self, player1, player2):
        if self.distance(player1) < 30 or self.distance(player2, 20) < 30:
            if self.horizontal_direction == "right":
                self.horizontal_direction = "left"
                self.after_hit_move()
            else:
                self.horizontal_direction = "right"
                self.after_hit_move()

    def after_hit_move(self):
        self.speed(1.3)
        new_y = self.ycor() + vertical_move[self.vertical_direction] * 3
        new_x = self.xcor() + horizontal_move[self.horizontal_direction] * 3
        self.goto(new_x, new_y)
        self.speed(2)