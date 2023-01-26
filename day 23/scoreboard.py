from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 260)
        self.hideturtle()
        self.write(arg='Score = 0', align='center', font=FONT)

    def display_score(self, level):
        self.clear()
        self.write(arg=f'Score = {level}', align='center', font=FONT)

    def game_over(self, level):
        self.clear()
        self.goto(0, 0)
        self.write(arg='Game Over', align='center', font=FONT)
        self.goto(0, -29)
        self.write(arg=f"Final Score: {level}", align='center', font= FONT)
