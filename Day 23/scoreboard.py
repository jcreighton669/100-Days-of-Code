from turtle import Turtle
FONT = ("Courier", 24, "normal")
STARTING_POSITION = (-250, 250)
ORIGIN = (0, 0)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(ORIGIN)
        self.write(f"GAME OVER", align="center", font=FONT)
