# create a random walk using turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
for _ in range(300):
    timmy.speed(100)
    timmy.width(4)
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
