import turtle
import random
from colour_pallet import colour_code

tim = turtle.Turtle()
s = turtle.Screen()
tim.pensize(3)
turtle.colormode(255)


def random_color():
    tim.color(random.choice(colour_code))


def forward():
    random_color()
    tim.fd(10)


def backward():
    random_color()
    tim.back(10)


def clockwise():
    random_color()
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def counter_clockwise():
    random_color()
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def pen_up():
    tim.pu()

def pen_down():
    tim.pd()

def clear_drawing():
    tim.clear()

s.listen()
s.onkey(forward, "w")
s.onkey(backward, "s")
s.onkey(clockwise, "d")
s.onkey(counter_clockwise, "a")
s.onkey(pen_up, "Up")
s.onkey(pen_down, "Down")
s.onkey(clear_drawing, "c")

s.exitonclick()
