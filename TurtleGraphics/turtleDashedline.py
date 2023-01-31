from turtle import Turtle,Screen
tim=Turtle()
tim.pensize(5)
tim.color("blue")
s=Screen()
for _ in range(10):
    tim.forward(15)
    tim.penup()
    tim.forward(15)
    tim.pendown()


s.exitonclick()