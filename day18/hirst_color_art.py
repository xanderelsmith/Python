import turtle
import random
colorList=[(231,34,156),(23,134,13),(198,23,56),(3,65,211)]
turtle.colormode(255)
myPen=turtle.Turtle()
myPen.hideturtle()
myPen.up()
myPen.setheading(-135)
myPen.forward(300)
myPen.setheading(to_angle=0)
goLeft=False
def goUpandTurn(myPen, data,angle,isLastNum):
    if data%9==0 and data>0:
        myPen.setheading(to_angle=90)        
        myPen.forward(50)
        if isLastNum:
            myPen.dot(10, random.choice(colorList))     
            
        myPen.setheading(angle)
        print('assigning')
        

for data in range(0,100):
    
    if(data==0):
        new_var=data
    else:
        new_var =data%len(colorList)
    print(new_var)
    myPen.dot(10,colorList[new_var])
    goUpandTurn(myPen, data,0 if goLeft else -180,data != 99)
    if data%9==0 and data>0:
        goLeft=not goLeft
        print(goLeft) 
    myPen.forward(50)
    
    print(goLeft)
newScreen=turtle.Screen()
newScreen.exitonclick()