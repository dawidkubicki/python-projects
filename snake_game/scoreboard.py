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
        self.high_score = self.read_high_score()
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt", mode="r") as f:
            return f.read()

    def update_high_score(self, score):
        with open("data.txt", mode="w") as f:
            f.write(str(score))

    def update_scoreboard(self):
        msg = "Score: " + str(self.score) + " High Score: " + self.read_high_score()
        self.clear()
        self.write(msg, font=STYLE, align=ALIGNMENT)

    def reset(self):
        if self.score > int(self.high_score):
            self.update_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto((0,0))
    #     self.write("GAME OVER", font=STYLE, align="center")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

