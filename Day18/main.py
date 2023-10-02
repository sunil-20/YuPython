# Turtle module
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")


def corner():
    timmy.forward(100)
    timmy.right(90)
    # screen = Screen()
    # screen.exitonclick()


def square():
    corner()
    corner()
    corner()
    corner()
    screen = Screen()
    screen.exitonclick()


# square()

# using for loop
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
