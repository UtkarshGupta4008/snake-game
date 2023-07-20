from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.different_turtles = []
        self.create_snake()
        self.head = self.different_turtles[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_different_turtles(i)

    def add_different_turtles(self, i):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(i)
        self.different_turtles.append(new_turtle)

    def extend(self):
        self.add_different_turtles(self.different_turtles[-1].position())

    def move(self):
        for run in range(len(self.different_turtles) - 1, 0, -1):
            new_x = self.different_turtles[run - 1].xcor()
            new_y = self.different_turtles[run - 1].ycor()
            self.different_turtles[run].goto(new_x, new_y)
        self.different_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

