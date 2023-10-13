from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y = y_position[i])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win!, The turtle color is {winning_color}.")
            else:
                print(f"You lose!, The turtle color is {winning_color}.")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()