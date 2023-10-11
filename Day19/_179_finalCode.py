from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y = y_position[i])
    


screen.exitonclick()