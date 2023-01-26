from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneko Game")
screen.tracer(0)
chosen_difficuly = {"hard":0.06, "normal":0.1, "easy":0.2}
difficulty = screen.textinput(
    title="Please choose a difficulty", prompt="hard , normal , easy"
).lower()
difficulty = chosen_difficuly[difficulty]

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.face_up, "Up")
screen.onkey(my_snake.face_down, "Down")
screen.onkey(my_snake.face_right, "Right")
screen.onkey(my_snake.face_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(difficulty)

    my_snake.move()
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.update_score()

    if my_snake.wall_collision_check() or my_snake.self_eat_check():
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()

