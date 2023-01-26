from car import Car
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
import time

level = 0
player = Player()
cars = Car()

# sets the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Car Game")

# setting up a scoreboard
scoreboard = Scoreboard()

# sets screen input
screen.listen()

# makes the screen refresh only when called
screen.tracer(False)

# listens to a keystroke to move the player up
screen.onkey(player.move_player, "Up")

cars.set_speed(level)
count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    if count % (6 - level) == 0:
        cars.spawn()
    if player.die_check(cars.car_list):
        game_is_on = False
        scoreboard.game_over(level)
    if player.win_check():
        level += 1
        cars.reset_level()
        scoreboard.display_score(level)
        cars.set_speed(level)




    count += 1



screen.exitonclick()