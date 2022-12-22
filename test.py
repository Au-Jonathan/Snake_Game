import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=699, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Create turtle
starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)


# Create snake food

# Detect collision with food

# Create a scoreboard

# Detect collision wall

# Detect collision with tail
screen.exitonclick()



