from turtle import Turtle

FONT = ("Courier", 22, "normal")
SCORE_POSITION = (-220, 265)
HIGH_SCORE_POSITION = (190, 265)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(arg=f"Level: {self.score}", align='center', font=FONT)
        self.goto(HIGH_SCORE_POSITION)
        self.write(arg=f"High Score: {self.high_score}", align='center', font=FONT)


    def add_score(self):
        self.score += 1

    def game_over(self):
        self.clear()

        if self.score > self.high_score:
            with open('data.txt', mode='w') as data:
                data.write(str(self.score))

        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=FONT)
