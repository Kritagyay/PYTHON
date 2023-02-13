import turtle
Turtle_Cordinates = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head=self.turtle_list[0]

    def create_snake(self):
        for position in Turtle_Cordinates:
           self.add_segment(position)

    def add_segment(self,position):
        new_turtle = turtle.Turtle(shape="circle")
        new_turtle.color("green")
        new_turtle.pu()
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for segment in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[segment - 1].xcor()
            new_y = self.turtle_list[segment - 1].ycor()
            self.turtle_list[segment].goto(new_x, new_y)
        self.head.fd(20)

    def reset(self):
        for seg in self.turtle_list:
            seg.goto(154447,52465)
        self.turtle_list.clear()
        self.create_snake()
        self.head=self.turtle_list[0]


    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
