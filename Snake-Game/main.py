from turtle import Turtle, Screen
import time
from snake import Snake
from FOOD import Food
from scorecard import Scorecard
screen=Screen()
screen.setup(800,800)
screen.bgpic("bg2.png")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scorecard=Scorecard()
game_is_on = True
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.blocks[0].distance(food )<15:
        food.refresh()
        scorecard.refresh()
        snake.extend_snake()
    if snake.blocks[0].xcor()>350 or snake.blocks[0].xcor() < -350 or snake.blocks[0].ycor()>350 or snake.blocks[0].ycor() < -350:
        scorecard.update()
        snake.update()
    for block in snake.blocks[1:]:
      if block.distance(snake.blocks[0]) < 15:
            snake.update()
            scorecard.update()

screen.exitonclick()