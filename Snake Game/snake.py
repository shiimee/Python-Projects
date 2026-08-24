from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        # TODO: Create Snake body
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape('square')
        snake.color('white')
        snake.goto(position)
        self.snakes.append(snake)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 100)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        self.add_segment(self.snakes[-1].pos())


    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1):
            position = self.snakes[seg_num - 1].pos()
            self.snakes[seg_num].goto(position)
        self.snakes[0].forward(MOVE_DISTANCE)

    #TODO: Allow snake to change direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

