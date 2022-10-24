from turtle import Screen
from car_manager import CarManager
from player import Player
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.colormode(255)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkeypress(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car and it moves.
    car_manager.create_car()
    car_manager.move()

    # Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    # Detect player hit the finish line of screen and reset position.
    if player.detect_hit_finish_line():
        player.reset_position()

        # Game is level up and the increase cars speed.
        score_board.level_up()
        car_manager.increase_car_speed()

screen.exitonclick()
