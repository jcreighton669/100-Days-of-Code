from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        with open("../File_Directory_Practice/data.txt") as data:
            self.high_score = int(data.read())
        self.color("Cyan")
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("../File_Directory_Practice/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
