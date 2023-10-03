# Draw a Spirograph
import random
import turtle

timmy = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.pencolor(random_color())
timmy.speed("fastest")
timmy.circle(100)

screen = turtle.Screen()
screen.exitonclick()
