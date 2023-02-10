import turtle
tim=turtle.Turtle()
screen=turtle.Screen()
screen.tracer(8, 25)
dist = 2
for i in range(200):
    tim.fd(dist)
    tim.rt(90)
    dist += 2


screen.exitonclick()