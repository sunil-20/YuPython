# Draw a Spirograph
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed(1)
timmy.circle(100)

screen = Screen()
screen.exitonclick()
