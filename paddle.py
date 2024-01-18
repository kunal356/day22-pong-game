from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,starting_pos):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(starting_pos)

    def up(self):
        y_cords = self.ycor() + 20
        self.goto(self.xcor(), y_cords)

    def down(self):
        y_cords = self.ycor() - 20
        self.goto(self.xcor(), y_cords)
