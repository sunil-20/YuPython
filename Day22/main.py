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
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    #time.sleep(0.1)
    screen.update()
    ball.move()
    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)< 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detech R paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
    # detect l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()









screen.exitonclick()