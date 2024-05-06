import pygame
import math
import random
from sport_car import SportCar
from passenger_car import PassengerCar
from company_car import CompanyCar


class Traffic:
    coordinates_car = ((1220, 270, 80, 40), (0, 350, 80, 40), (650, 620, 40, 80), (574, 0, 40, 80))

    def __init__(self):
        self._car_arr = []
        self._random_count_car = 4   # Первоначально 4 машинки

    # Создать массив машин
    def create_car_arr(self):
        self.car0 = PassengerCar(*self.coordinates_car[0])
        self.car1 = SportCar(*self.coordinates_car[1])
        self.car2 = PassengerCar(*self.coordinates_car[2])
        self.car3 = CompanyCar(*self.coordinates_car[3])
        self._car_arr.append(self.car0)
        self._car_arr.append(self.car1)
        self._car_arr.append(self.car2)
        self._car_arr.append(self.car3)

    # Прорисовка массива машин
    def draw_array(self):
        for car in self._car_arr:
            car.draw()
