import turtle
import time
from cars import cars
from Player import Player
from Score_Board import ScoreBoard

# tim=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("white")
s.setup(height=600,width=600)

s.tracer(0)

player_1=Player()
diff_car=cars()
score_card=ScoreBoard()

s.listen()
s.onkey(player_1.move_up,"w")

end_of_game=True
while end_of_game:
    time.sleep(0.1)
    s.update()
    diff_car.Create_car()
    diff_car.movement_car()

    for car in diff_car.car_list:
        if player_1.distance(car)<28:
            end_of_game=False
            score_card.Game_Over()
            print(f"Game Over,Your current level is {score_card.score}")

    if player_1.ycor()>280:
        score_card.increase_score()
        player_1.finish_line()
        diff_car.increase_speed()








s.exitonclick()