from turtle import Turtle

FONT = ('Courier', 13, 'normal')


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.current_level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f'Current Level : {self.current_level}', font=FONT)

    def level_up(self):
        self.current_level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER..!', align='center', font=('Consoles', 18, 'normal'))

    def demo(self):
        pass
    