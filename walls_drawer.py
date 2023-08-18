from turtle import Turtle

wall_coordinates = {
    'left': -390,
    'right': 370,
    'top': 390,
    'bottom': -370
}


class WallsDrawer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.draw_walls()

    def draw_walls(self):
        self.penup()
        self.goto(x=wall_coordinates['left'], y=wall_coordinates['bottom'])
        self.pendown()
        self.goto(x=wall_coordinates['left'], y=wall_coordinates['top'])
        self.goto(x=wall_coordinates['right'], y=wall_coordinates['top'])
        self.goto(x=wall_coordinates['right'], y=wall_coordinates['bottom'])
        self.goto(x=wall_coordinates['left'], y=wall_coordinates['bottom'])
