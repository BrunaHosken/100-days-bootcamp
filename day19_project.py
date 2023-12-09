#Etch-A-Sketch

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)
def move_backwards():
    turtle.backward(10)
def clear():
    turtle.reset()

def turn_right():
    turtle.right(10)
def turn_left():
    turtle.left(10)

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()