from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(8)
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r,g,b)
    return random_color

degrees = [0, 90, 180, 360]

def forward():
    return tim.forward(10)


for _ in range(200):
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(random.choice(degrees))


screen = Screen()
screen.exitonclick()
