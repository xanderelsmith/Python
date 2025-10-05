from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score=0
        super().__init__()
        self.write(f'Score:{self.score}')
    
    
    
    def updateScoreBoard(self):
        self.clear()
        
    def incrementScoreValue(self):
        self.score+=1
        