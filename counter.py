from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Counter(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")

    def countdown(self):
        for seconds in range(3, 0, -1):
            self.clear()
            self.write(f"{seconds}...", align=ALIGNMENT, font=FONT)
            time.sleep(1)
        self.clear()
