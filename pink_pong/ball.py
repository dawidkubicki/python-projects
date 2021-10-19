from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def detect(self):
        _, y_pos = self.pos()
        print(y_pos)
        if y_pos > 290:
            print("hit up")
            self.goto((0, 0))

        if y_pos < -290:
            self.goto((0, 0))
            print("hit down")