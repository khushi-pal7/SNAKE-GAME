import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(700,600)
screen.title("THE SNAKE GAME")
screen.tracer(0)

snake=Snake()
food=Food()
scorehere=scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#move
game_on=True
while(game_on):
    screen.update()
    time.sleep(0.1)
    snake.move()
#snake with food
    if snake.head.distance(food)<18:
        food.refresh()
        scorehere.inc_score()
        snake.extend()

#snake with wall
    if snake.head.ycor()>295 or snake.head.ycor()<-295 or snake.head.xcor()>345 or snake.head.xcor()<-345:
        game_on=False
        scorehere.gameover()

#snake with itself
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg)<10:
            game_on=False
            scorehere.gameover()


screen.exitonclick()