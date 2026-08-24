from turtle import Turtle

class Matchline(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        y = -230
        self.penup()
        self.goto(x=0, y=y)
        self.seth(90)
        self.color('white')
        while y < 220:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
            y += 30