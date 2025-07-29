# import screen
from turtle import Turtle, Screen
turtle=Turtle('turtle')


def moveRight():    
    direction=turtle.heading()-10
    turtle.setheading(direction)
    
def moveLeft():
    direction=turtle.heading()+10
    turtle.setheading(direction)
    
def moveForward():    
    turtle.forward(25)
    
def moveBackward():
    turtle.backward(25)
    
    
    
def clear():
    turtle.home()
    turtle.clear()
    
screen = Screen()


screen.listen()
screen.onkeypress(moveForward,'w')
screen.onkeypress(moveBackward,'x')
screen.onkeypress(moveLeft,'a')
screen.onkeypress(moveRight,'d')
screen.onkeypress(clear,'space')



screen.exitonclick()





