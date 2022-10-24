from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
MOVEMENT = 10


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.reset_position()

    def go_up(self):
        self.forward(MOVEMENT)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def detect_hit_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def play(self):
        pass
