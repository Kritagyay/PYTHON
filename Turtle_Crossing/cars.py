import turtle
import random
turtle.colormode(255)
MOVE_DISTANCE=5
INCREASE_PACE=5
COLOUR_LIST=["aliceblue","chocolate","blue","red","blueviolet","tan","grey","limegreen","violet","hotpink","yellow","tomato","cyan"]

class cars():
    def __init__(self):
        self.car_list=[]
        self.speed=MOVE_DISTANCE

    def Create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=turtle.Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.pu()
            new_car.y_cor=random.randint(-280,280)
            new_car.goto(280,new_car.y_cor)
            new_car.color(random.choice(COLOUR_LIST))
            self.car_list.append(new_car)

    def movement_car(self):
        for car in self.car_list:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed+=INCREASE_PACE