import random
import turtle as t
from turtle import Turtle, Screen


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


t.colormode(255)
justin = Turtle()
justin.speed("fastest")

for i in range(0, 360, 5):
    justin.setheading(i)
    justin.color(random_color())
    justin.circle(100)


for i in range(0, 360, 5):
    justin.setheading(i)
    justin.color(random_color())
    justin.circle(150)


for i in range(0, 360, 5):
    justin.setheading(i)
    justin.color(random_color())
    justin.circle(50)


my_screen = Screen()
my_screen.exitonclick()
