import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

#screen commands
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title('Turtle Crossing Game')

player = Player()
car_manager = CarManager()

#Scoreboard management
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

#Allow turtle to move
screen.onkeypress(key='Up', fun=player.move_forward)
screen.onkeypress(key='Down', fun=player.move_backwards)

game_is_on = True
while game_is_on:
    screen.update()

    #TODO Create car and move car
    car_manager.create_car()
    car_manager.move_car()
    time.sleep(0.1)

    #reset and go next level
    if player.ycor() >= FINISH_LINE_Y:
        player.player_reset()
        scoreboard.add_score()
        scoreboard.update_scoreboard()

        #Increase car speed
        car_manager.increase_speed()

        # Detect turtle collision with car (car is 20 (height) by 40 (length)
    for car in car_manager.list_of_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Delete turtle from list when reach x cor
    car_manager.stop_car()

screen.exitonclick()