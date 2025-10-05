
import time
from ball import Ball
from turtle import Screen

from scoreboard import ScoreBoard
from utils import SCREEN_WIDTH,SCREEN_HEIGHT
from paddle import Paddle

screen=Screen()
screen.bgcolor('black')
screen.screensize(canvwidth=SCREEN_WIDTH,canvheight=SCREEN_HEIGHT)
width = (screen.window_width()/2)-30
height=(screen.window_height()/2)-30
scoreboard=ScoreBoard(heightPosition=height-50)
ball= Ball()
extreemPaddleEnd = (SCREEN_WIDTH/2)-50
screen.tracer(0)
l_paddle=Paddle(position=(extreemPaddleEnd,0))
r_paddle=Paddle(position=(-extreemPaddleEnd,0))
screen.onkeypress(l_paddle.goUp,'Up')
screen.onkeypress(l_paddle.goDown,'Down')
screen.onkeypress(r_paddle.goUp,'w')
screen.onkeypress(r_paddle.goDown,'s')
screen.listen()
game_is_on=True

while game_is_on:    
    time.sleep(ball.ballSpeed)    
    screen.update()
    ball.move(screen=screen)
    
    # bounce with up or bottom
    if(ball.ycor()<-height or ball.ycor()>height):
        ball.bounce_y()
        
    distancewithPaddle = 25
    # bounce of paddle
    if((ball.distance(l_paddle)<distancewithPaddle and ball.xcor()>-extreemPaddleEnd) or( ball.distance(r_paddle)<distancewithPaddle and ball.xcor()<extreemPaddleEnd)):
        ball.bounce_x()
        
    # reset of r_side paddle
    if(ball.xcor() > width ): 
        scoreboard.counterLeft()           
        ball.reset_position_after_loss()
        
    # reset of l_side paddle
    if(ball.xcor()<-width):
        scoreboard.counterRight()  
        ball.reset_position_after_loss()





screen.exitonclick()