import turtle

class Block(turtle.Turtle):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=width / 20)
        self.penup()
        self.goto(x, y)
        self.width = width  # Adicione esta linha
        self.height = height  # Adicione esta linha

