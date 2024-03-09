# player.py

import turtle
from bullet import Bullet

class Player:
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shape("triangle")
        self.player.color("white")
        self.player.shapesize(stretch_wid=1, stretch_len=3)
        self.player.penup()
        self.player.goto(0, -250)

    def move_left(self):
        x = self.player.xcor()
        if x > -280:
            x -= 20
        self.player.setx(x)

    def move_right(self):
        x = self.player.xcor()
        if x < 280:
            x += 20
        self.player.setx(x)

    def move_up(self):
        y = self.player.ycor()
        if y < 280:
            y += 20
        self.player.sety(y)

    def shoot(self):
        bullet = Bullet(self.player.xcor(), self.player.ycor())
        return bullet

    def update(self):
        self.player.setheading(90)  # Set the player's orientation to face upwards
