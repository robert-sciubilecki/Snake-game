from turtle import Screen, Turtle
from walls_drawer import WallsDrawer
import time
from snake import Snake
from food import Food
from info import Display

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

walls_drawer = WallsDrawer()

display = Display()
def game():

    snake = Snake()
    screen.listen()
    keys_to_listen = ['Up', 'Down', 'Left', 'Right']
    for key in keys_to_listen:
        screen.onkey(lambda key_event=key: snake.turn(snake.head.heading(), key_event), key)
    food_obj = Food(snake.body)
    display.display_score()
    while True:
        tail_x, tail_y = snake.body[-1].position()
        food = food_obj
        snake.head_tracker()
        snake.move()
        if snake.check_collision_with_itself() or snake.check_collision_with_wall():
            display.game_over()
            screen.onkey(lambda: restart(snake, food, display), 'y')
            screen.onkey(exit_game, 'n')
            break
        x_head, y_head = snake.head.position()
        x_food, y_food = food.position()
        if round(x_head) == round(x_food) and round(y_head) == round(y_food):
            snake.eat_food(food=food, snake_end=(tail_x, tail_y))
            display.score += 1
            display.display_score()
            food_obj = Food(snake.body)
        screen.update()
        time.sleep(0.15)


def restart(snake, food, display):
    for seg in snake.body:
        seg.goto(x=1000, y=1000)
    food.goto(x=1000, y=1000)
    display.clear()
    screen.onkey(None, 'y')
    screen.onkey(None, 'n')
    game()


def exit_game():
    screen.bye()
    return


game()
screen.exitonclick()
