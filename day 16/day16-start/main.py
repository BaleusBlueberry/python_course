# from turtle import Turtle, Screen
# import turtle
#
# my_screen = Screen()
# timy = Turtle()
# timy.color("DeepSkyBlue")
#
# for i in range(0,6):
#     timy.forward(100)
#     timy.left(45)
#     timy.forward(40)
#     timy.left(45)
#     timy.forward(400)
#
# print(my_screen)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["cute furries", "cuteness level", "my bf"]
table.add_row(["baleus", 10, "me"])
table.add_row(["siphen", 10, "yes"])
table.add_row(["kin", 5, "no"])
table.add_row(["herzel", 6, "no"])
table.align["cute furries"] = "l"

print(table)
