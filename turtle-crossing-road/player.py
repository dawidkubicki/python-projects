from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.restart_position()
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)

    def restart_position(self):
        self.goto(STARTING_POSITION)

    def has_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
