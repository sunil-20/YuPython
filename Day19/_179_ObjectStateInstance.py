# Object state and Instances.
from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle()
tim.width = 4
jim = Turtle()
kelly = Turtle()
miya = Turtle()
pix = 500
tim.color = "green"
jim.color = "purple"
kelly.color = "blue"

def move_forward():
    screen.listen()
    screen.onkey(key = "w", fun = move_forward)
    #tim.forward(random.randint(10, 20))
    jim.forward(random.randint(10, 20))
    kelly.forward(random.randint(10, 20))
    miya.forward(random.randint(10, 20))
    screen.exitonclick()

move_forward()

screen.exitonclick()

    
