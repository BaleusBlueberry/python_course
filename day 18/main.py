import turtle
import random
import colorgram

# image_colors = colorgram.extract("image.jpg", 23)
# colors = []
#
# for color in image_colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   colors.append(new_color)
#
# print (colors)

color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57),
              (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138),
              (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
              (141, 171, 155), (179, 201, 186), (172, 153, 159)]

tim = turtle.Turtle()
tim.shape("arrow")
turtle.colormode(255)
tim.speed(0)
position = tim.position()
print(position)
tim.penup()


x = -500
y = -500

tim.goto(x, y)
for r in range(10):
    for i in range(10):
        x += 50
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.goto(x, y)
    x = -500
    y += 50
    tim.setpos(x, y)



screen = turtle.Screen()
screen.exitonclick()





# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# def change_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r,g,b


# for i in range(3, 10):
#
#     tim.color(change_color())
#     angle = 360 / i
#     for r in range(i):
#         tim.forward(40)
#         tim.right(angle)

# while tim != 1:
#     tim.color(change_color())
#     tim.right(random.choice(angle))
#     tim.forward(30)

# for g in range(360):
#     tim.color(change_color())
#     tim.left(2)
#     tim.circle(100)
