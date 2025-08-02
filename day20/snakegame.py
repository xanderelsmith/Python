from turtle  import Turtle, Screen
import time
from model.snakeclass import Snake
desktopScreen= Screen()
desktopScreen.setup(width=600,height=400,)
desktopScreen.title('Snake Game')
desktopScreen.bgcolor('black')

desktopScreen.tracer(0)
snake=Snake()
 
game_is_on=True



desktopScreen.listen()


desktopScreen.onkey(snake.moveUpward,'Up')
desktopScreen.onkey(snake.moveDownward,'Down')
desktopScreen.onkey(snake.moveLeft,'Left')
desktopScreen.onkey(snake.moveRight,'Right')


while game_is_on:
    desktopScreen.update()
    time.sleep(0.1)        
    snake.move()
    snake.isOutsideScreen(desktopScreen)     
    # screenwidth checker

    
    
        
            
            
        
        
    





desktopScreen.exitonclick()        
        
            
            
        
        
    





desktopScreen.exitonclick()