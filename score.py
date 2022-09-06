from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.value = 0
        super().__init__()
        self.hideturtle()
        self.color("green")
        self.penup()
        self.goto(-50, 280)
        self.clear()
        self.write(f"Score: {self.value}", font=("courier", 20, "normal"))
    def game_over(self):
        self.goto(-70,20)
        self.color("red")
        self.write("Game Over", font=("courier", 30, "normal"))

