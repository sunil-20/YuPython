# Object state and Instances.
from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle()
jim = Turtle()
kelly = Turtle()
miya = Turtle()
pix = 500

def move_forward():
    tim.forward(random.randint(10, 20))
    jim.forward(random.randint(10, 20))
    kelly.forward(random.randint(10, 20))
    miya.forward(random.randint(10, 20))
    screen.exitonclick()

move_forward()

screen.exitonclick()

    
