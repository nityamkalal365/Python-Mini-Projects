from turtle import Turtle, Screen
import random
COLORS = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "cyan",
    "magenta",
    "brown",
    "black",
    "white",
    "gray",
    "gold",
    "silver",
    "navy",
    "lime",
    "turquoise",
    "maroon",
    "violet"
]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(x=random_x, y=random_y)
