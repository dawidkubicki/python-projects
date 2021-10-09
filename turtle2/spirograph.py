import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

size_of_gap = 2

for _ in range(int(360/size_of_gap)):
    tim.circle(200)
    tim.setheading(tim.heading() + size_of_gap)
    tim.color(random_color())


screen = Screen()
screen.exitonclick()
