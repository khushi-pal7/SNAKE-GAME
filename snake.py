from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS=20
class Snake():
    # SNAKE BODY

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for pos in POSITION:
            self.add_segment(pos)

    def add_segment(self,pos):
        new_turtle = Turtle("square")
        new_turtle.color("yellow")
        #new_turtle.shapesize(0.8,0.8)
        new_turtle.penup()
        new_turtle.goto(pos)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            newx=self.segments[seg-1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



