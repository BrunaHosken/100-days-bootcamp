# Pong game

from turtle import Screen
from pong_game_files.paddle import Paddle
from pong_game_files.ball import Ball
from pong_game_files.scoreboard import Scoreboard
import time 

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))    

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down,"s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if(ball.xcor() > 380): 
        scoreboard.increse_l_player_score()
        ball.refresh()

    if (ball.xcor() < -380):
        scoreboard.increse_r_player_score()
        ball.refresh()

screen.exitonclick()