import random
from turtle import Turtle


COLORS=['red','orange','yellow','green','blue','purple']
STARTING_MOVE_DISTANCE=6
MOVE_INCREMENT=10

class CarManager(Turtle):
    def __init__(self):
        super.__init__()
        self.cars:list[Turtle]=[]
        for data in range(20):
            car=Turtle('square')
            car.color(random.shuffle())
            car.shapesize(stretch_wid=2)
            car.goto()
            self.cars.append(car)
        
            