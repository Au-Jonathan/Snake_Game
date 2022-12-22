from turtle import Turtle
starting_positions = [(0,0), (-20,0), (-40,0)]
move_distance = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() # When ever calling snake class, will create 3 turtles of 3 starting positions
        self.head = self.segments[0] # So that below no need to always specify self.segments[0]


    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        new_x = self.segments[len(self.segments) - 1].xcor()
        new_y = self.segments[len(self.segments) - 1].ycor()
        self.add_segment((new_x, new_y))
        #OR
        #self.add_segment(self.segments[-1].position())


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # def __init__(self):
    #     self.segments = []
    #     self.create_snake() # When ever calling snake class, will create 3 turtles of 3 starting positions
    #     self.head = self.segments[0] # So that below no need to always specify self.segments[0]
    #
    # def create_snake(self):
    #     for position in starting_positions:
    #         new_segment = Turtle("square")
    #         new_segment.color("white")
    #         new_segment.penup()
    #         new_segment.goto(position)
    #         self.segments.append(new_segment)
    #
    #
    # def move(self):
    #     for seg_num in range(len(self.segments) - 1, 0, -1):
    #         new_x = self.segments[seg_num - 1].xcor()
    #         new_y = self.segments[seg_num - 1].ycor()
    #         self.segments[seg_num].goto(new_x, new_y)
    #     self.head.forward(move_distance)
    #
    # def up(self):
    #     if self.head.heading() != DOWN:
    #         self.head.setheading(UP)
    #
    # def down(self):
    #     if self.head.heading() != UP:
    #         self.head.setheading(DOWN)
    #
    # def left(self):
    #     if self.head.heading() != RIGHT:
    #         self.head.setheading(LEFT)
    #
    # def right(self):
    #     if self.head.heading() != LEFT:
    #         self.head.setheading(RIGHT)


