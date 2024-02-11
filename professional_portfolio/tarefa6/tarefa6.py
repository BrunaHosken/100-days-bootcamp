# Using Python Turtle, build a clone of the 80s hit game Breakout.

import turtle
import time

# Configuração da janela
window = turtle.Screen()
window.title("Breakout Clone")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Barra do jogador
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Bola
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Função para mover a barra para a esquerda
def move_left():
    x = paddle.xcor()
    if x > -250:
        x -= 20
    paddle.setx(x)

# Função para mover a barra para a direita
def move_right():
    x = paddle.xcor()
    if x < 240:
        x += 20
    paddle.setx(x)

# Teclado
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Loop principal do jogo
while True:
    window.update()

    # Movimento da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Verifica colisões com as bordas
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Verifica colisão com a barra
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Verifica se a bola saiu da tela (perda do jogo)
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    time.sleep(0.01)  # Adiciona um pequeno atraso para controlar a velocidade do jogo
