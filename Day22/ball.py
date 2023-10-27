# moving ball
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
    def move(self):
        new_x = self.xcor()+ 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        
# detecting collision to wall
    def move(self):
        new_x = self.xcor() + self.x_move()
        new_y = self.ycor() + self.y_move()
        self.goto(new_x, new_y)