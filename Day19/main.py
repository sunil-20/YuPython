from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
# W = Forward,
# S = Backwards, 
# A = Counter_Clock, 
# D = Clockwise
# C = Clear drawing
# create a function for movement
def move_forward():
    tim.forward(50)
def move_backward():
    tim.backward(50)
def counter_clock():
    tim.left(50)

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    screen.listen()
    tim.pendown()
    
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = counter_clock)
screen.onkey(key = "c", fun = clear_screen)



screen.exitonclick()