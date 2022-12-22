import time
from turtle import Screen
from TurtleClass import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=699, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create Snake
snake = Snake()
# Create snake food
food = Food()
# Create Scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


# Detect collision with food, then extend tail
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()


# Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_over()


# Detect collision with tail
    for pos in snake.segments[1:]:
        if snake.head.distance(pos) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()


screen.exitonclick()
