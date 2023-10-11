from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win: ")
print(user_bet)
colors = []

tim = Turtle()
tim.penup()
tim.goto(x=-240, y = 0)

screen.exitonclick()