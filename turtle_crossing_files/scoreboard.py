from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0     
        self.penup() 
        self.goto(-270, 250)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}",font = FONT)

    def increse_score(self):
        self.score +=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = FONT)