from turtle import Turtle, Screen

justin = Turtle()
screen = Screen()


def move_forward():
    justin.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
