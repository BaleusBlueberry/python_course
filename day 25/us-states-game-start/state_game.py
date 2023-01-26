from turtle import Turtle, Screen
import csv
import pandas

font = ("Arial", 8, "normal")
data = pandas.read_csv("50_states.csv")
data_cov = data.copy()
data_cov.set_index("state", inplace=True)

class State_game():

    def __init__(self):
        self.state_list = []

    def create_state(self, user_choice):
        state = Turtle()
        state.speed(0)
        state.hideturtle()
        state.penup()
        state.color("black")
        self.state_list.append(state)
        x_cords = data_cov.loc[user_choice]["x"]
        y_cords = data_cov.loc[user_choice]["y"]
        state.goto(x_cords, y_cords)
        state.write(arg=user_choice)



    def check_state(self,user_imput):
        if user_imput in data["state"].unique():
            return True
        else:
            return False
