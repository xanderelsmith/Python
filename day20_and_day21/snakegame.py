from turtle  import Turtle, Screen
import time

from model.food import Food
from model.snakeclass import Snake


desktopScreen= Screen()
desktopScreen.setup(width=600,height=400,)
desktopScreen.title('Snake Xenzia')
desktopScreen.bgcolor('pink')

desktopScreen.tracer(0)
snake=Snake()
 
game_is_on=True



desktopScreen.listen()


desktopScreen.onkey(snake.moveUpward,'Up')
desktopScreen.onkey(snake.moveDownward,'Down')
desktopScreen.onkey(snake.moveLeft,'Left')
desktopScreen.onkey(snake.moveRight,'Right')

food=Food()
while game_is_on:
    desktopScreen.update()
    time.sleep(0.1)        
    snake.move()
    snake.isEatingFood(food)
    snake.isOutsideScreen(desktopScreen)     
    # screenwidth checker

    
    
        
            
            
        
        
    





desktopScreen.exitonclick()