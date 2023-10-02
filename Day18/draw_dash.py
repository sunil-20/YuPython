import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup()
timmy.setx(-300)
timmy.sety(10)
timmy.pendown()
#timmy.goto(-100, 1)

for i in range(50):
    timmy.pencolor("blue")
    timmy.forward(5)
    timmy.pencolor("white")
    timmy.forward(5)

screen = Screen()
screen.exitonclick()
