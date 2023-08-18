from turtle import Turtle


class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.goto(0, 30)
        self.write(f'GAME OVER', align='center', font=('Verdana', 30, 'bold'))
        self.goto(0, -30)
        self.write(f'Play again? (Y/N)', align='center', font=('Verdana', 15, 'normal'))

    def display_score(self, score):
        self.clear()
        self.goto(x=-300, y=400)
        self.write(f'Score: {score}', align='center', font=('Verdana', 20, 'normal'))

    def clear_display(self):
        self.clear()