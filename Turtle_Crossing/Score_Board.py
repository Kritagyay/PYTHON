from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-250,250)

        self.score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}",align='Left',font=('Arial',18,'normal'))

    def increase_score(self):
        self.score+=1
        self.update_score()

    def Game_Over(self):
        self.goto(0,0)
        self.write("GAME OVER ",align='Center',font=('Arial',18,'normal'))