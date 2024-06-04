from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score:{self.score}", align="center", font=("arial", 24, "normal"))

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("arial", 24, "normal"))
