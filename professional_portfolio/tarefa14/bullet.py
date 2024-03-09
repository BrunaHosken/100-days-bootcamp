# bullet.py

import turtle

class Bullet:
    def __init__(self, x, y):
        self.bullet = turtle.Turtle()
        self.bullet.shape("circle")
        self.bullet.color("yellow")
        self.bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.bullet.penup()
        self.bullet.goto(x, y)

    def update(self):
        y = self.bullet.ycor()
        y += 2  # Adjust the speed as needed
        self.bullet.sety(y)

    def is_collision(self, obj):
        distance = self.bullet.distance(obj)
        return distance < 15  # Adjust the collision threshold as needed
