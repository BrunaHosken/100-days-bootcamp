# Using Python Turtle, build a clone of the 80s hit game Breakout.

import turtle
import time
import random
from Paddle import Paddle
from Ball import Ball
from Block import Block

class BreakoutGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Breakout Clone")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        self.paddle = Paddle()
        self.ball = Ball()
        self.blocks = self.create_blocks()

        self.ball_speed = 0.005

        self.window.listen()
        self.window.onkeypress(self.paddle.move_left, "Left")
        self.window.onkeypress(self.paddle.move_right, "Right")

    def create_blocks(self):
        colors = ["blue", "green", "yellow", "orange", "red"]
        width = 80
        height = 20
        blocks = []

        for _ in range(5):
            x_cor = random.randint(-200, 200)
            y_cor = random.randint(100, 250)
            block = Block(random.choice(colors), width, height, x_cor, y_cor)
            blocks.append(block)

        return blocks

    def start_new_phase(self):
        for block in self.blocks:
            block.goto(1000, 1000)  # Move os blocos para fora da tela
        self.blocks = self.create_blocks()
        self.ball.goto(0, 0)  # Reseta a posição da bola
        self.ball.dx = 1  # Ajuste os valores conforme necessário
        self.ball.dy = -1  # Ajuste os valores conforme necessário

    def run_game(self):
        while True:
            self.window.update()

            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            if self.ball.xcor() > 290 or self.ball.xcor() < -290:
                self.ball.dx *= -1

            if self.ball.ycor() > 290:
                self.ball.dy *= -1

            if (self.ball.ycor() < -240 and self.ball.ycor() > -250) and \
                    (self.ball.xcor() > self.paddle.xcor() - 50 and self.ball.xcor() < self.paddle.xcor() + 50):
                self.ball.dy *= -1

            for block in self.blocks:
                if (block.ycor() + 20 > self.ball.ycor() > block.ycor() - 20) and \
                        (block.xcor() - block.width/2 < self.ball.xcor() < block.xcor() + block.width/2):
                    self.ball.dy *= -1
                    self.blocks.remove(block)
                    block.goto(1000, 1000)

            # Verifica se todos os blocos foram destruídos
            if not self.blocks:
                self.start_new_phase()

            if self.ball.ycor() < -290:
                self.start_new_phase()

            self.ball_speed *= 0.999
            time.sleep(self.ball_speed)

if __name__ == "__main__":
    game = BreakoutGame()
    game.run_game()

