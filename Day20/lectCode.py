# Snake game
from turtle import Screen, Turtle
import random
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_position = [(0, 0),(-20, 0), (-40, 0)]
segments = []
for i in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(i)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(5)


screen.exitonclick()
#time.sleep(1)