import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup()
timmy.setx(-300)
timmy.sety(50)
timmy.pendown()
#timmy.goto(-100, 1)

for i in range(50):
    timmy.pencolor("blue")
    timmy.forward(5)
    timmy.pencolor("white")
    timmy.forward(5)

tom = Turtle()
tom.shape('turtle')
for _ in range(15):
    tom.pendown()
    tom.pencolor("red")
    tom.forward(10)
    tom.penup()
    tom.forward(10)

screen = Screen()
screen.exitonclick()
