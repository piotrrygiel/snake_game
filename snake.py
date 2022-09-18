from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_length = 3
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for segment in STARTING_POSITIONS:
            self.add_segment(segment)

    def add_segment(self, position):
        snake_part = Turtle(shape="square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.goto(position)
        self.snake_body.append(snake_part)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_num - 1].xcor()
            new_y = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
