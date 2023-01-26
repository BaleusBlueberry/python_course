from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        """makes the body of the snake"""
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """creating the bace body of the snake"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color("White")
        new_segment.penup()
        new_segment.speed(0)
        new_segment.goto(position)
        new_segment.shape("square")
        self.snake_body.append(new_segment)

    def extend(self):
        """extends the snake"""
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        """makes the snake move"""
        for part in range((len(self.snake_body) - 1), 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def face_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def face_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def face_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def face_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def wall_collision_check(self):
        if self.head.xcor() < -300 or self.head.xcor() > 300 or self.head.ycor() < -300 or self.head.ycor() > 280:
            return True
        else:
            return False

    def self_eat_check(self):
        for snake_part in self.snake_body[1:]:

            if self.head.distance(snake_part) < 10:
                return True

