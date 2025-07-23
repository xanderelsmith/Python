from turtle import Turtle, Screen

import heroes as heroes

def moveDottedLine(
    emma_turtle:Turtle):
    emma_turtle.pendown()
    emma_turtle.forward(5)
    emma_turtle.penup()
    emma_turtle.forward(5)
def moveAndturnRight(emma_turtle,angle):
    emma_turtle.forward(50)
    emma_turtle.right(angle)
def paintMultipleShapes(emma_turtle:Turtle,):
    lastshapeindex = 20
    first_shape_index = 3
    for index in range(first_shape_index,lastshapeindex):
        angleValue=360/index
        for i in range(index):
            moveAndturnRight(emma_turtle,angleValue)
        


emma_turtle=Turtle()
emma_turtle.shape('turtle')
emma_turtle.color('red')





paintMultipleShapes(emma_turtle=emma_turtle)


print(heroes.gen())

desktop_screen=Screen()
desktop_screen.exitonclick()

