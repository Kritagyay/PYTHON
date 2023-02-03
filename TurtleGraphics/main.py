from turtle import Turtle,Screen
import random
t=Turtle()
s=Screen()
# s.bgcolor("black ")
t.pencolor("blue")
t.pensize(5)
# t.circle(100,steps=3)
# t.circle(120,steps=4)
# t.circle(140,steps=5)
# t.circle(160,steps=6)
# t.circle(180,steps=7)
# t.circle(200,steps=8)

colours=["indigo","lime green","orange red","medium spring green","yellow","violet","lime"]

def shapes(sides):
    angle=360/sides
    for _ in range (sides):
        t.forward(100)
        t.rt(angle)
for i in range (3,11):
    t.color(random.choice(colours))
    shapes(i)


s.exitonclick()