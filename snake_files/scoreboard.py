from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.open_file()
        self.color("white")
        self.penup() 
        self.goto(0, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.highscore}", align = ALIGNMENT, font = FONT)

    def increse_score(self):
        self.score +=1
        self.clear()
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_file()
        self.score = 0
        self.update()
        

    def open_file(self):
        with open("./snake_files/data.txt") as file:
            self.highscore = int(file.read())  

    def update_file(self):
        with open("./snake_files/data.txt", mode="w") as file:
            file.write(f"{self.highscore}") 