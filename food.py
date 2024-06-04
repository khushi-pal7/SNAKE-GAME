import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.6,0.6)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x = random.randint(-300, 300)
        y = random.randint(-260, 260)
        self.goto(x, y)


    