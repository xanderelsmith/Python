from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self,heightPosition:int):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color('white')
        self.penup()
        self.hideturtle() 
        self.goto(0,heightPosition)
        self.write(f'{self.l_score}:{self.r_score}',align="center",font=("Courier",50,"normal"))
    def counterLeft(self):
        self.l_score+=1
        self.updateScore()
    def counterRight(self):
        self.r_score+=1
        self.updateScore()
    def updateScore(self):
        self.clear()
        self.write(f'{self.l_score}:{self.r_score}',align="center",font=("Courier",50,"normal"))
        