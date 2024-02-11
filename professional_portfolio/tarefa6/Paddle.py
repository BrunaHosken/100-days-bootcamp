import turtle

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        x = self.xcor()
        if x > -250:
            x -= 20
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        if x < 240:
            x += 20
        self.setx(x)
