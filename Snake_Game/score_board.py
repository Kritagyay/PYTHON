from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.pu()
        self.goto(0,395)
        self.hideturtle()
        self.update()
        self.increase_speed=0.13


    def update(self):
        self.clear()
        self.write(f"Scoreboard:{self.score} HighScore:{self.highscore}", False, align='center', font=('Arial', 15, 'bold'))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open ("data.txt", mode='w') as file:
                file.write(f"{self.highscore}")
        self.score=0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align='center', font=('Product Sans',20,'bold'))

    def increase_score(self):
        self.score+=1
        self.increase_speed*=0.9
        self.update()
