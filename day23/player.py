from turtle import Turtle


STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE=280
SCREEN_HEIGHT=600
class Player(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        half_Height_loc = (SCREEN_HEIGHT/2)-30
        self.goto(0,-half_Height_loc)
    def move_up(self):
        xcor=self.xcor()
        ycor=self.ycor()
        self.goto(xcor,ycor+10)
    def move_left(self):
        xcor=self.xcor()
        ycor=self.ycor()
        self.goto(xcor-10,ycor)
    def move_right(self):
        xcor=self.xcor()
        ycor=self.ycor()
        self.goto(xcor+10,ycor)
        