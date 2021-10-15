from turtle import Turtle

ALIGNMENT = "center"
STYLE = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        msg = "Score: " + str(self.score)
        self.clear()
        self.write(msg, font=STYLE, align=ALIGNMENT)

    def game_over(self):
        self.goto((0,0))
        self.write("GAME OVER", font=STYLE, align="center")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

