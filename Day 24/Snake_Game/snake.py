import sys
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """Initialize the snake constructor."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a starting snake for the game."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        """Function to move the snake forward smoothly according to the heading of the head."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Move/navigate the snake UP the screen"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move/navigate the snake DOWN the screen"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move/navigate the snake LEFT the screen"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move/navigate the snake RIGHT the screen"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Adds a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle(shape="circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
