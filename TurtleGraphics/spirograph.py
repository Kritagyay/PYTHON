import turtle
import random
tim=turtle.Turtle()
tim.speed(15)
s=turtle.Screen()
turtle.colormode(255)
tim.pensize(2)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    my_colour=(r,g,b)
    return(my_colour)


def draw_spiro(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size)

draw_spiro(5)


s.exitonclick()