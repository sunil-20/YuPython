# Snake game
from turtle import Screen, Turtle
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_value= [0, -20, -40]
for i in range(0, 3):
    tim = Turtle(shape = "square")
    tim.color("white")
    tim.shape("square")
    tim.goto(x= x_value[i], y=0)

# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_position = [-100, -50, 0, 50, 100, 150]
# all_turtles = []
# for i in range(0, 6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.penup()
#     new_turtle.color(colors[i])
#     new_turtle.goto(x=-230, y = y_position[i])
#     all_turtles.append(new_turtle)
# if user_bet:
#     is_race_on = True

screen.exitonclick()