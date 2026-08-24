from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from matchline import Matchline
import time


#TODO 1: Create the screen
screen = Screen()
screen.bgcolor('black')
screen.title('My Pong Game')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
matchline = Matchline()

screen.onkeypress(key='Up', fun=r_paddle.move_up)
screen.onkeypress(key='Down', fun=r_paddle.move_down)

screen.onkeypress(key='w', fun=l_paddle.move_up)
screen.onkeypress(key='s', fun=l_paddle.move_down)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.y_bounce()

    #detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() == 330 or ball.distance(l_paddle) < 60 and ball.xcor() == -330:
        ball.x_bounce()

    #detect collision with wall
    if ball.xcor() == 380 or ball.xcor() == -380:
        time.sleep(0.5)

        #right paddle
        if ball.xcor() == 380:
            ball.reset_ball(x_reset= -10)
            scoreboard.add_score_l()
            scoreboard.update_scoreboard()
        #left paddle
        else:
            ball.reset_ball(x_reset=10)
            scoreboard.add_score_r()
            scoreboard.update_scoreboard()

    #game over
    if scoreboard.l_score == 3 or scoreboard.r_score == 3:
        scoreboard.game_over()
        is_game_on = False

    ball.move()

screen.exitonclick()