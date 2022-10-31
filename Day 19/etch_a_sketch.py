from turtle import Turtle, Screen


def move_forward():
    justin.forward(10)


def move_backward():
    justin.backward(10)


def move_count_clockwise():
    justin.left(10)
    justin.forward(10)


def move_clockwise():
    justin.right(10)
    justin.forward(10)


def clear_screen():
    justin.reset()


justin = Turtle()
screen = Screen()
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_count_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
