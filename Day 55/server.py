from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

print(random_number)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/z1HdiobjzYIrm/giphy.gif">'


@app.route("/<int:number>")
def guess_number(number):
    if number < random_number:
        return '<h1 style="color: purple;">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if number == random_number:
        return '<h1 style="color: gold;>You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    if number > random_number:
        return '<h1 style="color: blue;>Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
