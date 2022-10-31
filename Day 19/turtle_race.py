from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle color will win the race").lower()
color = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
all_turtles = []
x_start = -230
y_start = -70


def generate_distance():
    return random.randint(1, 10)


for i in color:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(str(i))
    new_turtle.penup()
    new_turtle.goto(x_start, y_start)
    y_start += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 210:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won the bet! The {winning_turtle} turtle won the race.")
            else:
                print(f"Sorry, you lost the winning turtle is {winning_turtle} turtle.")
            is_race_on = False
        turtle.forward(generate_distance())


screen.exitonclick()
