# Turtle crossing game

import time
from turtle import Screen
from turtle_crossing_files.player import Player
from turtle_crossing_files.car_manager import CarManager
from turtle_crossing_files.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()   

screen.listen()
screen.onkeypress(player.go_up, "Up")

scoreboard = Scoreboard()

car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for car_index in car.all_cars:
        if player.distance(car_index) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        scoreboard.increse_score()
        player.go_to_start()
        car.speed_up()

screen.exitonclick()