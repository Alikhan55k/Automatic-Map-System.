from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Scores={score}/50", align="center", font=("Arial", 15, "bold"))
    def increase(self,score):
        self.clear()
        self.write(f"Scores={score}/50", align="center", font=("Arial", 15, "bold"))
        self.clear()
