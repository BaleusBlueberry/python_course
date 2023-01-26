from turtle import Turtle
from turtle import Screen
from pong import Pong
from ball import Ball
import time

game_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer()

ball = Ball()
right_pog = Pong(350, 0)
left_pog = Pong(-350, 0)

# screen inputs
screen.listen()
screen.onkey(right_pog.move_up, 'Up')
screen.onkey(right_pog.move_down, 'Down')
screen.onkey(left_pog.move_up, 'w')
screen.onkey(left_pog.move_down, 's')

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.detect_wall_collision()
    ball.detect_player_collision(right_pog, left_pog)
    ball.move()


screen.exitonclick()
