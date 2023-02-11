from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("blue")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")


    def refresh(self):
        rand_x = random.randint(-330, 330)
        rand_y = random.randint(-330, 330)
        self.goto(rand_x, rand_y)
