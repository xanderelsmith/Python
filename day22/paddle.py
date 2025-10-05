from turtle import Turtle

from utils import SCREEN_HEIGHT

class Paddle(Turtle):
    def __init__(self,position:tuple):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.goto(position)
        self.shapesize(stretch_wid=3,stretch_len=1)
    
    def goUp(self):
        new_var = self.ycor()
        newYCor = new_var+20
        if newYCor<(SCREEN_HEIGHT/2):
            self.goto(self.xcor(),newYCor)
    def goDown(self):
        new_var = self.ycor()
        newYCor = new_var-20
        if newYCor>-(SCREEN_HEIGHT/2):
            self.goto(self.xcor(),newYCor)
        
        