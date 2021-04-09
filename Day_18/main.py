from turtle import Turtle, Screen, colormode
from random import randint, shuffle, choice

screen = Screen()

turt = Turtle()
# turt.width(10)
turt.speed(0)
colormode(255)


def pick_color():
    # colors = ["blue", "black", "brown", "red", "yellow", "green", "orange", "beige", "turquoise", "pink"]
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colors = (r, g, b)
    return colors

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        rand_color = pick_color()
        turt.circle(100)
        turt.setheading(turt.heading() + size_of_gap)

        turt.fillcolor(rand_color)
        turt.color(rand_color)

draw_spirograph(1)

# This moves the turtle in random directions and with random colors
# for _ in range(300):
#     angles = [0, 90, 180, 270]
#     turt.forward(30)
#     turt.setheading(choice(angles))
#     rand_color = pick_color()
#     turt.fillcolor(rand_color)
#     turt.color(rand_color)




# How to draw shapes. User inputs number of shapes they want to draw, then the turtle will draw them in order
# timmy_the_turtle = Turtle()
#
# screen = Screen()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("teal")
#
# num_of_shapes = int(input("How many shapes do you want to draw? "))
#
#
#
# def shape(shapes):
#     angles = 3
#     sides = 3
#     for _ in range(shapes):
#         for _ in range(sides):
#             rand_color = pick_color()
#             timmy_the_turtle.fillcolor(rand_color)
#             timmy_the_turtle.color(rand_color)
#             timmy_the_turtle.forward(100)
#             timmy_the_turtle.right(360/angles)
#         angles += 1
#         sides += 1
#
# shape(num_of_shapes)







# This needs to stay at the bottom
screen.exitonclick()