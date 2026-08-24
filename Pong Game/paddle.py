from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_cor):
        super().__init__()
        self.create_paddle(starting_cor)
    def create_paddle(self, starting_cor):
        self.shape('square')
        self.color('white')
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(starting_cor)

    #TODO 2: Create paddle and allow it to move
    def move_up(self):
        self.seth(90)
        self.forward(20)

    def move_down(self):
        self.seth(270)
        self.forward(20)
