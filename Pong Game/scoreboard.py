from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=self.r_score, align='center', font=('Courier', 80, 'normal'))

    def add_score_r(self):
        self.r_score += 1

    def add_score_l(self):
        self.l_score += 1

    def game_over(self):
        self.clear()
        self.goto(x=0, y=240)
        if self.l_score == 3:
            self.write(arg='Left Player Wins!', align='center', font=('Courier', 40, 'normal'))
        elif self.r_score == 3:
            self.write(arg='Right Player Wins!', align='center', font=('Courier', 40, 'normal'))