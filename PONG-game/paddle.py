from turtle import Turtle


class Paddle:
    def __init__(self,position):
        self.block = Turtle()

        self.make_paddle(self.block,position)
    def make_paddle(self, paddle, position):


        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=1, stretch_len=5)
        paddle.penup()
        paddle.setheading(90)
        paddle.goto(position)



    def up(self):
        new_y=self.block.ycor() + 20
        self.block.goto(self.block.xcor(),new_y)
    def down(self):
        new_y = self.block.ycor() - 20
        self.block.goto(self.block.xcor(), new_y)