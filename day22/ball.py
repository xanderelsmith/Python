import time
from turtle import Turtle, TurtleScreen


class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape('circle')
        self.ballSpeed=0.1
        self.color('white')
        self.penup()
        self.y_move=10
        self.x_move=10
        self.home()
    def move(self,screen:TurtleScreen):
        # print(f'{str(self)}')
        new_x=self.xcor()+ self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
                     
            
    def bounce_y(self):
        self.y_move*= -1
        new_x=self.xcor()+ self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_x(self):
        self.x_move*= -1
        if(self.ballSpeed<1):
            self.ballSpeed-=0.008
        new_x=self.xcor()+ self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def reset_position_after_loss(self):
        self.home()
        self.bounce_x() 
        self.ballSpeed=0.1
        
        
    # def __str__(self):
    #     return f'{self.speed()}'
        
            
        
     
        
    