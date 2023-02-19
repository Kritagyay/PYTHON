from turtle import Turtle
import random
class Ball_play(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.fillcolor()
        self.pu()
        self.shape("circle")
        self.xcor_move=10
        self.ycor_move=10
        self.increase_speed=0.1

    def movement(self):
        new_x=self.xcor()+self.xcor_move
        new_y=self.ycor()+self.ycor_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ycor_move*=-1

    def bounce_x(self):
        self.xcor_move*=-1
        self.increase_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.increase_speed=0.1
        self.bounce_x()
