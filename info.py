from turtle import Turtle


class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        with open('./h_score.txt') as file:
            self.high_score = int(file.read())

    def game_over(self):
        self.goto(0, 30)
        self.write(f'GAME OVER', align='center', font=('Verdana', 30, 'bold'))
        self.goto(0, -30)
        self.write(f'Play again? (Y/N)', align='center', font=('Verdana', 15, 'normal'))
        if self.score > self.high_score:
            self.high_score = self.score
            with open('h_score.txt', mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0

    def display_score(self):
        self.clear()
        self.goto(x=-350, y=400)
        self.write(f'Score: {self.score} High score: {self.high_score}', align='left', font=('Verdana', 20, 'normal'))
