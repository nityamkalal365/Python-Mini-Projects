from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)
right_paddle=Paddle((350,0))
left_paddle=Paddle((-360,0))
ball=Ball()
scorecard=Scorecard()


game_on=True
screen.listen()
screen.onkey(fun=right_paddle.up,key="Up")
screen.onkey(fun=right_paddle.down,key="Down")
screen.onkey(fun=left_paddle.up,key="w")
screen.onkey(fun=left_paddle.down,key="s")

while game_on:
    time.sleep(ball.move_speed)


    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(left_paddle.block)<50 and ball.xcor()<-330 or ball.distance(right_paddle.block)<50 and ball.xcor()>320:
        ball.bounce_x()
    if ball.xcor()>340:
        scorecard.r_point()
        ball.reset()

    if ball.xcor()<-340:
        scorecard.l_point()
        ball.reset()








screen.exitonclick()