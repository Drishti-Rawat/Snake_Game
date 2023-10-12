# Snake Game
'''
1) create a snake body
2) move the snake
3) control the snake
4) detect collision with food
5) create a scoreboard
6) detect collision with wall
7) detect collision with tail
'''



import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score=scoreboard.Scoreboard()
score.update_score()

screen.listen()

screen.onkey(key="Up" , fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

#     detect coolison with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

#     detect collision with wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

# Detect collision with tail
    for segment in snake.segments[1: ]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()


screen.exitonclick()