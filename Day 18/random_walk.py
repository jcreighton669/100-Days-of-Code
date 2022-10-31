import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
j_turtle = Turtle()
j_turtle.shape("turtle")
j_turtle.pensize(10)
j_turtle.speed("fastest")
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


for i in range(1000):
    j_turtle.color(random_color())
    # j_turtle.color(random.choice(turtle_colors))
    j_turtle.setheading(random.choice(directions))
    j_turtle.forward(20)

my_screen = Screen()
my_screen.exitonclick()
