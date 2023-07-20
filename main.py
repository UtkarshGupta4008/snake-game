from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.setup(width=590, height=590)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
eat_food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(eat_food) < 15:
        eat_food.refresh()
        snake.extend()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() > 295 or snake.head.ycor() < -285:
        is_game_on = False
        score.game_over()

    # Detect collision with wall
    for i in snake.different_turtles[1:]:
        if snake.head.distance(i) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
