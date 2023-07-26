import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import Random
class CarManager(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.selected_color = random.choice(COLORS)
        self.color(self.selected_color)
        self.shapesize(stretch_wid = 2, stretch_len = 1)
        self.setheading(90)
        self.goto(position)
        self.first_pos = position
        self.speed = STARTING_MOVE_DISTANCE


    def move(self):
        self.goto(self.xcor() - self.speed, self.ycor())

    def accelerate(self):
        self.speed += MOVE_INCREMENT


    def collide(self):
        self.speed = STARTING_MOVE_DISTANCE