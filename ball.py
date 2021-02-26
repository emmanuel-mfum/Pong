from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):  # reversing the y direction
        self.y_move *= -1

    def bounce_x(self):  # reversing the x direction
        self.x_move *= -1
        self.move_speed *= 0.9  # increase the speed everytime it bounces along the x-axis

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # reset the speed in order for it not to increase indefinitely
        self.bounce_x()  # reverse the x-axis
