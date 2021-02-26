from turtle import Turtle


UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.setposition(position)
        self.speed("fastest")

    def up(self):
        current_y = self.ycor()
        new_y = current_y + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        current_y = self.ycor()
        new_y = current_y - 20
        self.goto(self.xcor(), new_y)


