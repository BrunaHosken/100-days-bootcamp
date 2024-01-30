#day 19
#Order Functions & Event Listeners

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

screen.listen()
screen.onkey(key = "space", fun = move_forwards)
screen.exitonclick()