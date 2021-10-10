from turtle import Turtle, Screen

tim = Turtle()


screen = Screen()
screen.listen()

def forwards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def counterClockwise():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)

def clears():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counterClockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clears)


screen.exitonclick()
