from turtle import Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.x = x
        self.head = None
        self.create()

    def create(self):
        if self.x == 0:
            self.shape('square')
            self.setheading(UP)
            self.speed('fastest')
            self.penup()
            self.goto(-350, 0)
            self.turtlesize(stretch_len=5, stretch_wid=1)
            self.color('white')

        if self.x == 1:
                self.shape('square')
                self.setheading(UP)
                self.speed('fastest')
                self.penup()
                self.goto(350, 0)
                self.turtlesize(stretch_len=5, stretch_wid=1)
                self.color('white')


    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)
