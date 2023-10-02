# create a random walk using turtle with random colors
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
direction = [0, 90, 180, 270]


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(300):
    timmy.speed(100)
    timmy.width(4)
    timmy.color(rand_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
