import turtle
import random
from distance import dist
from colour import colour_list

s=turtle.Screen()
s.setup(height=700,width=700)

user_bet=s.textinput(title="Turtle Betting Race", prompt="Choose which colour turtle will win ?")
# print(user_bet)

turtle_list=[]

for index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colour_list[index])
    new_turtle.pu()
    new_turtle.goto(x=-330, y=dist[index])
    turtle_list.append(new_turtle)

if user_bet:
    end_of_race = False

while not end_of_race:
    for turtle in turtle_list:
        if turtle.xcor()>330:
            end_of_race=True
            winning_turtle=turtle.pencolor()
            if user_bet==winning_turtle:
                print(f"You Win , Your {winning_turtle} turtle has won.")
            else:
                print(f"You loose , The {winning_turtle} turtle has won.")

        turtle.forward(random.randint(0, 10))






s.exitonclick()