from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('blue')
screen.title('Pong')
screen.tracer(0)
line = Turtle()
line.speed('fastest')
line.hideturtle()
line.penup()
line.goto(0,-300)
line.color('white')


for i in range(30):
    line.pendown()
    line.setheading(90)
    line.forward(10)
    line.penup()
    line.forward(10)





player1 = Paddle(0)
player2 = Paddle(1)
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")

screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")

flag = True
player1_score = 0
player2_score = 0
i = 0.1
while flag:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.bounce_back()

    if ball.xcor() > 390:
        ball.reset()
        score.p1_score()

    if ball.xcor() < -390:
        ball.reset()
        score.p2_score()

screen.exitonclick()