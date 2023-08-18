from turtle import Turtle
from walls_drawer import wall_coordinates

DIRECTIONS = {
    'Up': 90,
    'Down': 270,
    'Left': 180,
    'Right': 0
}

OPPOSITE_DIR = {
    90: 270,
    270: 90,
    180: 0,
    0: 180
}


class Snake:
    def __init__(self):
        self.body = []
        self.head = None
        self.direction = None
        self.create_body()
        self.previous_head_position = None

    def create_body(self):
        for x_cor in range(0, 3):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(x=x_cor * 20, y=0)
            self.body.insert(0, segment)
        self.head = self.body[0]

    def move(self):
        x, y = None, None
        for seg in self.body:
            seg_x, seg_y = seg.position()
            if seg == self.head:
                seg.forward(distance=20)
            else:
                seg.goto(x=x, y=y)
            x, y = seg_x, seg_y

    def head_tracker(self):
        self.previous_head_position = {'x': round(self.head.xcor()),
                                       'y': round(self.head.ycor()),
                                       }

    def eat_food(self, food, snake_end):
        x, y = snake_end
        food.goto(x=x, y=y)
        self.body.append(food)

    def check_collision_with_itself(self):
        for segment in self.body[1:]:

            seg_x, seg_y = round(segment.xcor()), round(segment.ycor())
            head_x, head_y = round(self.head.xcor()), round(self.head.ycor())
            if [seg_x, seg_y] == [head_x, head_y]:
                return True

    def check_collision_with_wall(self):
        x_cor = self.head.xcor() + 10 if self.head.xcor() < 0 else self.head.xcor() - 10
        y_cor = self.head.ycor() + 10 if self.head.ycor() < 0 else self.head.ycor() - 10
        if round(y_cor) in (wall_coordinates['top'], wall_coordinates['bottom']):
            return True
        if round(x_cor) in (wall_coordinates['left'], wall_coordinates['right']):
            return True

    def skip(self, direction, too_tight):
        if too_tight:
            self.move()
            self.head.setheading(direction)
        else:
            self.head.setheading(direction)

    def turn(self, direction, key):
        prev_x_cor, prev_y_cor = self.previous_head_position.values()
        chosen_dir = DIRECTIONS[key]
        current_dir = round(direction)
        if chosen_dir != OPPOSITE_DIR[current_dir]:
            if chosen_dir == DIRECTIONS['Left'] or chosen_dir == DIRECTIONS['Right']:
                too_tight_turn = prev_y_cor == round(self.head.ycor())
                self.skip(chosen_dir, too_tight_turn)
            elif chosen_dir == DIRECTIONS['Up'] or chosen_dir == DIRECTIONS['Down']:
                too_tight_turn = prev_x_cor == round(self.head.xcor())
                self.skip(chosen_dir, too_tight_turn)
