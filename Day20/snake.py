from turtle import Screen, Turtle
import random
import time

X_VALUE = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in X_VALUE:
            tim = Turtle(shape = "square")
            tim.color("white")
            tim.penup()
            tim.goto(x= i, y=0)
            self.segments.append(tim)
    def move(self):
         
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

        
    def up(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)