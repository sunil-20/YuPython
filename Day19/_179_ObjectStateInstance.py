# Object state and Instances.
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title = "Make your bet!", prompt = "Which turtle will win the race?: ")
# print(user_bet)

tim = Turtle(shape= "turtle")
# tim.width = 4
tim.penup()
tim.goto(x = -240, y= 100 )

jim = Turtle(shape= "turtle")
# jim.width = 4
jim.penup()
jim.goto(x = -240, y= 50)

kelly = Turtle(shape= "turtle")
# kelly.width = 4
kelly.penup()
kelly.goto(x = -240, y= -0)

miya = Turtle(shape= "turtle")
# miya.width = 4
miya.penup()
miya.goto(x = -240, y=-50)
pix = 500

def move_forward():
    screen.listen()
    screen.onkey(key = "w", fun = move_forward)
    tim.color("green")
    tim.forward(random.randint(10, 20))
    jim.color("purple")
    jim.forward(random.randint(10, 20))
    kelly.color("blue")
    kelly.forward(random.randint(10, 20))
    miya.color("pink")
    miya.forward(random.randint(10, 20))
    screen.exitonclick()

move_forward()

screen.exitonclick()

    
