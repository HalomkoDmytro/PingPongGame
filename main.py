from turtle import Screen
import time

from ball import Ball
from playery import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

player_r = Player(350, 0)
player_l = Player(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_r.up, "Up")
screen.onkey(player_r.down, "Down")
screen.onkey(player_l.up, "w")
screen.onkey(player_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with player
    if (ball.distance(player_r) < 50 and ball.xcor() > 320) \
            or ball.distance(player_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
