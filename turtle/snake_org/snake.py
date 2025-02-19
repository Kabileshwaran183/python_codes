from turtle import *

SEGMENT_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for position in SEGMENT_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)
    
    def extend_segment(self):
        self.add_segment(self.segment[-1].position())
        
    def move_snake(self):
            for seg in range(len(self.segment)-1,0,-1) :
                new_x = self.segment[seg-1].xcor()
                new_y = self.segment[seg-1].ycor()
                self.segment[seg].goto(new_x,new_y)
            self.head.forward(MOVE_FORWARD)
    
    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP :
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)            
    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)
    def reset(self):
        for i in self.segment :
            i.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]



