from turtle import Turtle, Screen
import random

j_turtle = Turtle()

FORWARD_DISTANCE = 100
num_sides = [3, 4, 5, 6, 7, 8, 9, 10]
turn_angle = []
turtle_colors = ["red", "seashell", "sienna", "tan", "steelBlue", "MistyRose", "PaleGreen", "peru", "pink", "honeydew",
                 "gold", "DeepSkyBlue2"]


def get_angle(side_count):
    return round(360 / side_count, 2)


for side in num_sides:
    turn_angle.append(get_angle(side))

for num in num_sides:
    color_value = random.choice(turtle_colors)
    turtle_colors.remove(color_value)
    j_turtle.color(color_value)
    for _ in range(num):
        j_turtle.forward(FORWARD_DISTANCE)
        j_turtle.right(360 / num)

my_screen = Screen()
my_screen.colormode(255)
my_screen.exitonclick()
