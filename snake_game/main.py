from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game v.0.1")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

screen.exitonclick()
