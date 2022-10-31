import turtle as t

justin = t.Turtle()
justin.penup()
justin.goto(-250, 0)
justin.pendown()

for i in range(15):
    justin.forward(10)
    justin.penup()
    justin.forward(10)
    justin.pendown()


my_screen = t.Screen()
my_screen.exitonclick()
