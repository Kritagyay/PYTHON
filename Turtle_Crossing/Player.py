import turtle
import random
from turtle import Turtle
STARTING_POSITION=(0,-280)
FORWARD_DIST=10
turtle.colormode(255)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.r=random.randint(0,255)
        self.g=random.randint(0,255)
        self.b=random.randint(0,255)

        self.rgb=(self.r,self.g,self.b)
        self.color(self.rgb)
        self.fd(20)

    def finish_line(self):
        self.goto(STARTING_POSITION)