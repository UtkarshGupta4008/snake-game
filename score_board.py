from turtle import Turtle
ALIGNMENT = "Center"
FONT = ('courier', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=('courier', 25, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
