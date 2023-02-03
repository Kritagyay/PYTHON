import turtle
import colorgram
import random

tim=turtle.Turtle()
turtle.colormode(255)
s=turtle.Screen()
tim.speed(20)

s.bgcolor("white")

# colors=colorgram.extract('download.jpeg',30)
# rgb_color=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_color.append(new_color)

colour_code=[ (244, 235, 46), (196, 12, 34), (221, 159, 69),(43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22), (202, 34, 91),
             (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28), (227, 161, 9), (78, 212, 157), (67, 73, 221),
             (13, 95, 61), (78, 194, 225), (239, 158, 215), (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238)]

num_of_dots=100

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
tim.pd()
for dots in range(1,num_of_dots+1):
        tim.dot("20",random.choice(colour_code))
        tim.pu()
        tim.forward(50)
        tim.pd()

        if dots%10==0:
            tim.setheading(90)
            tim.pu()
            tim.fd(50)
            tim.setheading(180)
            tim.fd(500)
            tim.setheading(0)
            tim.pd()
# tim.hideturtle()
s.exitonclick()