from turtle import Turtle, Screen, colormode, fillcolor
from random import shuffle

# This was used to extract list of colors from image
# rgb = []
# colors = c.extract('dots.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)

# 20 in size, 10x10 grid

color_list = [(203, 10, 33), (245, 234, 50), (239, 234, 2), (219, 159, 74), (241, 36, 137), (41, 82, 176),
              (30, 39, 158), (37, 216, 59), (204, 72, 21), (22, 148, 26), (203, 32, 106), (182, 18, 10), (19, 18, 42),
              (223, 163, 8), (57, 15, 10), (218, 140, 194), (91, 8, 29), (65, 68, 231), (85, 209, 148), (77, 195, 227),
              (12, 95, 62), (239, 157, 214), (232, 69, 38), (88, 237, 205), (0, 250, 222), (253, 4, 43)]
turt = Turtle(visible=False)
turt.speed(0)
colormode(255)
x = -200
y = -200
turt.penup()
turt.goto(x, y)
turt.pendown()

for _ in range(10):
    for _ in range(10):
        shuffle(color_list)
        fillcolor(color_list[0])
        turt.color(color_list[0])

        turt.begin_fill()
        turt.circle(10)
        turt.end_fill()

        turt.penup()
        turt.forward(40)
        turt.pendown()
    turt.penup()
    y += 40
    turt.goto(x, y)
    turt.pendown()



screen = Screen()

screen.exitonclick()
