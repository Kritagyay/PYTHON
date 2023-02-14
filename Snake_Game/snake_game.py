import turtle
import time;
from snake_movement import Snake
from food import food
from score_board import Score

s = turtle.Screen()
s.bgcolor("black")
s.setup(height=845, width=1536)

s.title("Snake Game ")
s.tracer(0)

turtle_list = []
snake = Snake()
food = food()
score_card = Score()

s.listen()
s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")

end_of_game=False

while not end_of_game:
    s.update()
    time.sleep(score_card.increase_speed)
    snake.move()

    if snake.head.xcor() > 760 or snake.head.xcor() < -760 or snake.head.ycor() > 417 or snake.head.ycor()< -417:
        # end_of_game = True
        # score_card.game_over()
        score_card.reset()
        snake.reset()
        # print(f"Game Over,your highest score is {score_card.score}")

    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        score_card.increase_score()

    for segment in snake.turtle_list:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            # end_of_game = True
            # score_card.game_over()
            # print(f"Game Over,your highest score is {score_card.score}")
            score_card.reset()
            snake.reset()


s.exitonclick()
