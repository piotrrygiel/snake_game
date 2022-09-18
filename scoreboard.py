from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.ht()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Scoreboard: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update()

