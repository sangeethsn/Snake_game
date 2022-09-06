from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("yellow")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.segments[0].setheading(RIGHT)

    def up(self):
        if self.head.heading != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.segments[0].setheading(DOWN)
