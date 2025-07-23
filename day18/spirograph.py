import random
import turtle as t

pen = t.Turtle()
t.colormode(255)
def generateRgbColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def angelafunc(pen, generateRgbColor):
    for _ in range(int(360/5)):
        pen.speed('fastest')
        pen.pencolor(generateRgbColor())
        pen.circle(radius=50)     
        pen.setheading(pen.heading()+5)

        
        
        
angelafunc(pen, generateRgbColor)


pen.forward(240)





desktopScreen=t.Screen()
desktopScreen.exitonclick()

