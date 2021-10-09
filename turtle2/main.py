from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

size = 100

def triangle(size):
    degree = 360/3
    for _ in range(3):
        tim.forward(size)
        tim.right(degree)
        tim.forward(size)

def square(size):
    tim.color("pink")
    degree = 360/4
    tim.forward(size/2)
    for _ in range(4):
        tim.right(degree)
        tim.forward(size)
        
def pentagon(size):
    tim.color("green")
    degree = 360/5
    for _ in range(5):
        tim.right(degree)
        tim.forward(size)

def hexagon(size):
    tim.color("blue")
    degree = 360/6
    for _ in range(6):
        tim.right(degree)
        tim.forward(size)

def rest(size):
    tim.color("yellow")
    degree = 360/7
    for _ in range(7):
        tim.right(degree)
        tim.forward(size)
    tim.color("black")
    degree = 360/8
    for _ in range(8):
        tim.right(degree)
        tim.forward(size)
    tim.color("purple")
    degree = 360/9
    for _ in range(9):
        tim.right(degree)
        tim.forward(size)
    tim.color("orange")
    degree = 360/10
    for _ in range(10):
        tim.right(degree)
        tim.forward(size)

tim.left(90)
tim.penup()
tim.forward(330)
tim.right(90)
tim.pendown()

triangle(size)
square(size*2)
pentagon(size*2)
hexagon(size*2)
rest(size*2)


#for _ in range(20):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

#drwawing a square/rectangle
#for i in range(4):
#    tim.forward(100)
#    tim.lt(90)

screen = Screen()
screen.exitonclick()
