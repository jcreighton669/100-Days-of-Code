from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("Cyan")
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.penup()
        self.color("Crimson")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
