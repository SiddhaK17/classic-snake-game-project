from turtle import Turtle
                                                            #the default size of one box is 20px width and 20 px height
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]           #as the default size of one box is 20px x 20px, then to move it on the left we will do: -20 px on the x axis and 0px on y axis as it's on the same line
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):        #the code in here is going to determine what should happen when we initialize a new snake object
        self.segments = []     #remember we're going to need to use self when we are working within a class
        self.create_snake()
        self.head = self.segments[0]        #remember if you have this line of code above the "create_snake", it's probably gonna error out because at this point this segments is empty

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
