from turtle import Turtle


class Paddle(Turtle):  #so now all paddle objs can acess turtle obj and methods

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)



