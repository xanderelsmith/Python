from turtle import Screen, Turtle
move_distance = 20
class Snake :
    def __init__(self):
        # self.isATScreenExtent
        self.segments:list[Turtle]=[]
        for index in range(3):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(index*-20,0)
            
            self.segments.append(new_segment)
    def move(self):
        for index in range(len(self.segments)-1,0,-1):
            # print(index), stop variable(0) is not part of the generation, hence why we calll forward on first index
            axis_x=self.segments[index-1].xcor()                                             
            axis_y=self.segments[index-1].ycor()
            self.segments[index].goto(axis_x,axis_y)
        move_distance = 20
        self.segments[0].forward(move_distance)
        
        
    
    def moveUpward(self):
        self.segments[0].setheading(90)
    def moveDownward(self):
        self.segments[0].setheading(270)
    def moveLeft(self):
        self.segments[0].setheading(180)
    def moveRight(self):
        self.segments[0].setheading(0)

    def isOutsideScreen(self,desktopScreen:Screen):
        halfscreen = desktopScreen.window_width()/2
        if self.segments[0].xcor()> halfscreen:
            self.segments[0].goto(x=-halfscreen,y=0)
            
        
        
        