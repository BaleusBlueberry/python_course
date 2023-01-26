import random
from turtle import Turtle
from typing import List, Any

STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = -10
SPAWN_AREA = -240, 245
car_spawn_rate = [0, 0, 0, 0, 1, 2, 3]


def random_color():
    colors = [
        "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
        "cyan",
        "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray",
    ]
    return random.choice(colors)

class Car:

    def __init__(self):
        self.car_list = []
        self.spawn()

    def set_speed(self, level):
        self.move_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level

    def spawn(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random_color())
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.speed(0)
        new_car.goto(self.spawn_place)  # make the x position random at the beginning as well
        self.car_list.append(new_car)

        # temp :
        # if random.choice(car_spawn_rate) != 0:
        #     for i in range(random.choice(car_spawn_rate)):
        #         car = self.__init__(level)
        #         car_list.append(car)

    def move(self):

        for car in self.car_list:
            current_x = car.xcor()
            car.goto(current_x + self.move_speed, car.ycor())

    @property
    def spawn_place(self):
        #set the range where a new car can spawn at
        y_cord = random.randint(*SPAWN_AREA)
        x_cord = 300
        num_of_cars = len(self.car_list)

        if num_of_cars > 0:
            for i in range(num_of_cars):
                y = y_cord
                current_car = self.car_list[i]
                # check if the new spawned car is near a previous car
                current_y = abs(current_car.ycor())
                previous_y = abs(self.car_list[i - 1].ycor())
                result = current_y - previous_y
                if current_car.distance(self.car_list[i - 1]) < 40 and -25 < result < 25:
                    y_cord += random.choice([-30, 30])
                    if y < 0:
                        y += 40
                    elif y > 0:
                        y -= 40
                    return x_cord, y

        return x_cord, y_cord

    def reset_level(self):
        for car in self.car_list:
            car.goto(1000, 1000)
        self.car_list.clear()
