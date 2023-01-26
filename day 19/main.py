from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# def move_forwards():
#     tim.forward(20)
#
# def move_right():
#     tim.right(10)
#
# def move_left():
#     tim.left(10)
#
# def move_backwards():
#     tim.forward(-20)
#
# def clear_screen():
#     screen.resetscreen()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(move_backwards, "s")
# screen.onkey(clear_screen, "c")
# screen.exitonclick()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")

red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
magenta = Turtle()
