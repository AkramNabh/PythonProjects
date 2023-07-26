import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
the_player = Player()
cars = []

for _ in range (1, 20):
    first_car = CarManager((random.randint(300, 1300), random.randint(-250, 250)))
    cars.append(first_car)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()
        if car.xcor() < -340:
            car.setposition(car.first_pos)

        if car.distance(the_player) < 20:
            the_player.collided()
            game_is_on = False
    if the_player.ycor() > 280:
        the_player.collided()
        for car in cars:
            car.accelerate()
    screen.listen()
    screen.onkey(the_player.move_up,"w")

