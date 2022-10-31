from turtle import Turtle, Screen

justin_the_turtle = Turtle()
justin_the_turtle.color("SlateBlue")


for i in range(4):
    justin_the_turtle.forward(200)
    justin_the_turtle.right(90)


my_screen = Screen()
my_screen.exitonclick()
