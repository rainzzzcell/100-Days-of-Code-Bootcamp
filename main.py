import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Controller
screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #car creation
    car_manager.create_car()
    car_manager.move_cars()

    #faliure
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.next_level()

screen.exitonclick()