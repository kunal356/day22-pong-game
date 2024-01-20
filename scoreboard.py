from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, align="center", font=('Courier', 80, 'normal'))

    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
