from turtle import Turtle, Screen
import csv
import pandas
from state_game import State_game

data = pandas.read_csv("50_states.csv")


state_game = State_game()
screen = Screen()
screen.title("U.S game")
image = "blank_states_img.gif"
screen.bgpic(image)
game_is_on = True

list_of_choices = []
number_c = 0

while number_c < 49:
    user_choice = screen.textinput(title="Guess a state", prompt="what is a name of a state").lower().capitalize()
    if user_choice == "Exit":
        break
    if user_choice not in list_of_choices:
        list_of_choices.append(user_choice)
        if state_game.check_state(user_choice):
            state_game.create_state(user_choice)
            number_c += 1
    else:

        print("You already chose this state , choose something else please!")

state_names = list(data["state"])
remaining_states = [x for x in state_names if x not in list_of_choices]

data_frame = pandas.DataFrame(remaining_states, columns=["states"])
data_frame.to_csv("remaining states to remember.csv")

