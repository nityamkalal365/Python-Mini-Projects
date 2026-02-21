from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 18, "normal")
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.count=0
        with open("highscore.txt") as data:
            self.highscore=int(data.read())
        self.speed("fastest")
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.count} High Score: {self.highscore}",True,ALIGNMENT,font=FONT)

    def update(self):
        if self.highscore<self.count:
            self.highscore=self.count
            with open("highscore.txt",mode="w") as data:
                data.write(f"{self.highscore}")

        self.count=0
        self.refresh()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", True, ALIGNMENT, font=FONT)

    def refresh(self):
        self.count+=1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.count} High Score: {self.highscore}", True, ALIGNMENT, font=FONT)
