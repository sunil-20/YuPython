# ping pong
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# creating paddle on both sides of the screen
paddle = Turtle
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)


screen.exitonclick()