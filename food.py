from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # rand_x = random.randint(-280, 280)
        rand_x = random.randrange(-280, 280, 20)
        # rand_y = random.randint(-280, 280)
        rand_y = random.randrange(-280, 280, 20)
        self.goto(x=rand_x, y=rand_y)
