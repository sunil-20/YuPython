# ping pong
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball() # initialize ball object

# listen to keystroke
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()









screen.exitonclick()