from turtle import Turtle


class Player(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto((pos_x, pos_y))

    def up(self):
        self.goto(self.xcor(),
                  self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(),
                  self.ycor() - 20)
