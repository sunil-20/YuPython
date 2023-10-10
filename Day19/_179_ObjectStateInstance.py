# Object state and Instances.
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title = "Make your bet!", prompt = "Which turtle will win the race?: ")
# print(user_bet)

tim = Turtle()
tim.width = 4
tim.penup()
tim.goto(x = -240, y= 100 )

jim = Turtle()
jim.width = 4
jim.penup()
jim.goto(x = -240, y= 50)

kelly = Turtle()
kelly.width = 4
kelly.penup()
kelly.goto(x = -240, y= -0)

miya = Turtle()
miya.width = 4
miya.penup()
miya.goto(x = -240, y=-50)
pix = 500

tim.color = "green"
jim.color = "purple"
kelly.color = "blue"

def move_forward():
    screen.listen()
    screen.onkey(key = "w", fun = move_forward)
    tim.forward(random.randint(10, 20))
    jim.forward(random.randint(10, 20))
    kelly.forward(random.randint(10, 20))
    miya.forward(random.randint(10, 20))
    screen.exitonclick()

move_forward()

screen.exitonclick()

    
