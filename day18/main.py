from turtle import Turtle, Screen
# avoid writing code like {from turtle import *}

def moveAndturnRight(emma_turtle):
    emma_turtle.forward(100)
    emma_turtle.right(90)

emma_turtle=Turtle()
emma_turtle.shape('turtle')
emma_turtle.color('red')


for i in range(4):
    moveAndturnRight(emma_turtle)



desktop_screen=Screen()
desktop_screen.exitonclick()

