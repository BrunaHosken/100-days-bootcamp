# enemy.py

import turtle

class Enemy:
    def __init__(self, x, y):
        self.enemy = turtle.Turtle()
        self.enemy.shape("square")
        self.enemy.color("red")
        self.enemy.penup()
        self.enemy.goto(x, y)

    def update(self):
        y = self.enemy.ycor()
        y -= 0.1  # Adjust the speed as needed
        self.enemy.sety(y)
