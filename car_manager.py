from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(320, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
