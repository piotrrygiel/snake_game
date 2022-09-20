from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from counter import Counter
import time

snake_speeds = (0.2, 0.1, 0.05)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
difficulty = screen.numinput("Difficulty", "Choose difficulty: 1 - EASY, 2 - MEDIUM, 3 - HARD", 1, 1, 3)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
counter = Counter()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

for i in range(1, 4):
    if difficulty == i:
        snake_speed = snake_speeds[i-1]

counter.countdown()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(snake_speed)

    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -295 \
            or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
