from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.foodPower=10
        self.penup()
        self.color('red')
        self.shape('square')
        print('Created')
    def reset(self):
        self.goto(randint(0,600),randint(0,400))
    