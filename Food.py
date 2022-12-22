from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# from turtle import Turtle
# import random
#
# number_of_food = 3
#
#
# class Food(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.sgg = []
#         self.num_food()
#
#     def num_food(self):
#         for num in (0, number_of_food):
#             new_food = Food()
#             new_food.shape("circle")
#             new_food.penup()
#             new_food.shapesize(stretch_len=0.5, stretch_wid=0.5)
#             new_food.color("blue")
#             new_food.speed("fastest")
#
#             random_x = random.randint(-280, 280)
#             random_y = random.randint(-280, 280)
#             new_food.goto(random_x, random_y)
#             self.sgg.append(new_food)
