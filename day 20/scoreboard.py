from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 19, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Your score is: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"  Game over\nfinal score: {self.score}", align=ALIGNMENT, font=("Courier", 40, "normal"))

