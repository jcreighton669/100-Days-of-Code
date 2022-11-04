from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball to start the game/set."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Detects when the ball collides with the top or bottom of the court and deflects it."""
        self.y_move *= -1

    def bounce_x(self):
        """Detects when the ball collides with the left or right paddle and deflects it."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Sets the ball back in the center of the court after a point has been made."""
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
