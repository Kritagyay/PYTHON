import turtle
import random
turtle.colormode(255)
tim=turtle.Turtle()
s=turtle.Screen()


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    my_colour=(r,g,b)
    return (my_colour)




direction=[0,90,180,270]
tim.pensize(5)
tim.speed(15)

for i in range(300):

    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(direction))

    # tim.

s.exitonclick()