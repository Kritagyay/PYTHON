import turtle
# import random
import time

from paddle import Paddle
from Ball import Ball_play
from Scorre_board import Score

tim=turtle.Turtle()
s=turtle.Screen()
s.setup(height=600, width=800)
s.bgcolor("black")
s.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

s.listen()
s.onkey(r_paddle.up,"Up")
s.onkey(r_paddle.down,"Down")
s.onkey(l_paddle.up,"w")
s.onkey(l_paddle.down,"s")

ball=Ball_play()
score_card=Score()

end_of_game=True
while end_of_game:
    s.update()
    ball.movement()
    time.sleep(ball.increase_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score_card.l_point()

    if ball.xcor()< -370:
        ball.reset_position()
        score_card.r_point()

s.exitonclick()