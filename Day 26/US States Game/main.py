import pandas
import turtle

image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
correct_states = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

states_list = data.state.to_list()
guessed_states = []

# print(states_list)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_states += 1
        guessed_states.append(answer_state)

