from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtle = []

# tim.penup()
# tim.goto(x=-240, y=-100)

def set_position(turtle, x: int, y: int):
    turtle.penup()
    turtle.goto(x, y)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    set_position(new_turtle, x=-230, y=y_positions[turtle_index])

    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! Turtle {winning_color} was first.")
            else:
                print(f"You lost :( \nTurtle {winning_color} was first.")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
