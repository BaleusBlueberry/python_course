import csv

# with open("weather_data.csv") as structure:

#   data = structure.readlines()

#
# with open("weather_data.csv") as structure:
#     data = csv.reader(structure)
#
#     temperatures = []
#     for line in data:
#         if line[1] == 'temp':
#             pass
#         else:
#             line = int(float(line[1]))
#             temperatures.append(line)
#
# temperatures = temperatures[1:]
# print(temperatures)

import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # temperature_list = data["temp"].to_list()
# # avrage = round(sum(temperature_list) / len(temperature_list), 2)
# # print(avrage)
# # print(data.query("temp == temp.max()"))
#
# monday = data[data.day == "Monday"]
# temp = int(monday.temp)
# print(temp / 5)

# need to create list with grey , red , black , and their count

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

new_data = {
    "fur colors": ["Gray", "Cinnamon" , "Black"],
    "number of squesls": [grey, red, black],
}

finished = pandas.DataFrame(new_data)
finished.to_csv("squers are gay.csv")