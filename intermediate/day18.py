#day 18
# Turtle & the Graphical User Interface (GUI)

import turtle as t
import random

t.colormode(255)
colors= ["red", "orange", "yellow", "green", "blue", "indigo", "violet",
        "pink", "grey", "purple"] 
directions = [0, 90, 180, 270]

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    color = (r,g,b)
    return color

def make_shapes(angle, range_shape):
    for _ in range(range_shape):
        turtle.forward(100)
        turtle.left(angle)

def calc_shapes():
    angle = 360
    for i in range(3,11):
        turtle.color(random_color())
        make_shapes(turtle, angle/i, i)
    



def make_dashed_line():
    for _ in range(15):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)

def random_walk():
    for _ in range(200):
        color = random_color()
        width = random.randint(0, 10)
        direction = random.choice(directions)
        turtle.width(width)
        turtle.color(color)
        turtle.forward(50)
        turtle.setheading(direction)

def spirograph(size):
    for i in range(int(360/size)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() +size)
        


turtle = t.Turtle() 
turtle.shape("turtle")
turtle.speed('fastest')
# make_dashed_line()
# calc_shapes()
# random_walk()

spirograph(20)  

screen = t.Screen()
screen.exitonclick()
