from turtle import Turtle

POSITIONS  = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270



class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        
    def create_snake(self):
        for snake_index in POSITIONS:
            self.add_segment(snake_index)

    def move(self):
        for snake in range(len(self.snake_list) -1, 0, -1):
            new_x = self.snake_list[snake - 1].xcor()
            new_y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(new_x , new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def add_segment(self, position):
        snake = Turtle(shape = "square")
        snake.penup()
        snake.goto(position)
        snake.color("white")
        self.snake_list.append(snake)
    
    def reset(self):
        for snake in self.snake_list:
            snake.goto(1000,1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]