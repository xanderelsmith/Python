import random
from turtle import Turtle, Screen
isGameInSession=True
screen = Screen()
colours=['red','orange','yellow','green','blue','indigo','violet']
all_turtles=[]
screen.setup(width=600,height=400,)
inputtedData=screen.textinput(prompt="Make your bet",title="Which turtle will win the race? Enter a color:")
for index in range(len(colours)):
    turtle=Turtle('turtle')
    turtle.color(colours[index])
    turtle.penup()
    turtle.setpos(x=-280,y=150-(index*50))
    all_turtles.append(turtle)

while isGameInSession:
    for new_turtle in all_turtles:
        winningColor=new_turtle.pencolor()
        finishLineExtent=280
        random_variable=random.randint(0,10)
        new_turtle.forward(random_variable)
        if new_turtle.xcor()>finishLineExtent:
            isGameInSession=False
            if inputtedData==winningColor:                
                print(f'{new_turtle.pencolor()}, You won')
            else:
                print(f'{new_turtle.pencolor()}, You Lost')
                
            
            
screen.exitonclick()
