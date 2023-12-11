from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 60, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_player_score = 0
        self.l_player_score = 0      
        self.color("white")
        self.penup() 
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_player_score, align = ALIGNMENT, font = FONT)
        self.goto(100,200)
        self.write(self.r_player_score, align = ALIGNMENT, font = FONT)

    def increse_r_player_score(self):
        self.r_player_score +=1
        self.update()
    
    def increse_l_player_score(self):
        self.l_player_score +=1
        self.update()


        