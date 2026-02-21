from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self):

        self.blocks = []
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_blocks(position)
    def add_blocks(self,position):
        block = Turtle(shape="square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.blocks.append(block)
    def extend_snake(self):
        self.add_blocks(self.blocks[-1].position())
    def move(self):
        for block in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block - 1].xcor()
            new_y = self.blocks[block - 1].ycor()
            self.blocks[block].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTANCE)
    def update(self):
        for block in self.blocks:
            block.goto(1000,1000)
        self.blocks.clear()
        self.create_snake()

    def up(self):
        if self.blocks[0].heading()!=DOWN:
            self.blocks[0].setheading(90)
    def down(self):
        if self.blocks[0].heading() != UP:
            self.blocks[0].setheading(270)
    def right(self):
        if self.blocks[0].heading() != LEFT:
            self.blocks[0].setheading(0)
    def left(self):
        if self.blocks[0].heading() != RIGHT:
            self.blocks[0].setheading(180)