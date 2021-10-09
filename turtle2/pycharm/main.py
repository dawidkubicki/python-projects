import turtle as t
from turtle import Screen
import colorgram
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.pensize(2)
rgb_colors = []
colors = colorgram.extract('image.jpg', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


def random_color():
    color = random.choice(colors)
    return color.rgb.r, color.rgb.g, color.rgb.b


print(random_color())


def draw(space, x):
    for i in range(x):
        for j in range(x):
            tim.color(random_color())
            tim.dot()
            tim.forward(space)
        tim.backward(space * x)

        tim.left(90)
        tim.forward(space)
        tim.right(90)


tim.penup()
draw(10, 10)
tim.hideturtle()

screen = Screen()
screen.exitonclick()
