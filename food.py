from turtle import Turtle
from random import choice

CORS_X = [cor for cor in range(-380, 361, 20)]
CORS_Y = [cor for cor in range(-360, 381, 20)]


class Food(Turtle):
    def __init__(self, snake_body):
        super().__init__()
        self.available_x_cor = None
        self.available_y_cor = None
        self.exclude_snake_from_available_coordinates(snake_body)
        self.put_food_on_screen()

    def put_food_on_screen(self):
        self.shape('square')
        self.penup()
        self.color('white')
        self.goto(x=choice(self.available_x_cor), y=choice(self.available_y_cor))

    def exclude_snake_from_available_coordinates(self, snake_body):
        for segment in snake_body:
            x, y = segment.position()
            self.available_x_cor = [cor for cor in CORS_X if cor != x]
            self.available_y_cor = [cor for cor in CORS_Y if cor != y]
