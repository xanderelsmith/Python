import random
from turtle import Turtle, Screen

colors = ['CornflowerBlue', 'DarkOrchid', "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen",]
angle = [0, 90, 180, 270]

def generateRgbColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def goRandomDir(pen: Turtle):
    while True:
        pen.pensize(15)
        pen.speed('fastest')
        pen.pencolor(generateRgbColor())  # <-- Call the function
        forward = random.choice(angle)
        pen.setheading(forward)
        pen.forward(30)

pen = Turtle()
pen.shape()
pen.color('red')

desktop_screen = Screen()
desktop_screen.colormode(255)  # <-- Add this line for RGB support

goRandomDir(pen)
desktop_screen.exitonclick()