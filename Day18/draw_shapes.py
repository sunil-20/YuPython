# draw different shapes using turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shapes():
    for i in range(3, 11):
        angle = 360 / i
        timmy.color(random.choice(colors))
        for _ in range(i):
            timmy.forward(100)
            timmy.right(angle)


draw_shapes()
screen = Screen()
screen.exitonclick()
