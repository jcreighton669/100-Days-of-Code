import random
import turtle as t
from turtle import Turtle, Screen
import colorgram


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


t.colormode(255)
justin = Turtle()
justin.speed("fastest")
justin.penup()
starting_x = -250

for i in range(starting_x, 250, 50):
    justin.setx(starting_x)
    justin.sety(i)
    for j in range(10):
        justin.color(random.choice(rgb_colors))
        justin.dot(20)
        justin.forward(50)


my_screen = Screen()
my_screen.exitonclick()
