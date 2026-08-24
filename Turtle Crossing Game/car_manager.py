from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.list_of_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_control = 6

    def create_car(self):
        random_chance = random.randint(1, self.car_control)
        if random_chance == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.seth(180)
            color = random.choice(COLORS)
            car.color(color)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.list_of_cars.append(car)

    def move_car(self):
        for cars in self.list_of_cars:
            cars.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        if self.car_control != 3:
            self.car_control -= 1

    def stop_car(self):
        for car in self.list_of_cars:
            if car.xcor() <= -320:
                self.list_of_cars.remove(car)




