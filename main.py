from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        print("you crushed")
        food.refresh()
        snake.extend()
        scoreboard.refresh_score()

    # COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # COLLISION WITH TAIL
    for part in snake.snakes[1:]:
        # if part == snake.head:
        #     pass
        if snake.head.distance(part) < 15:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
