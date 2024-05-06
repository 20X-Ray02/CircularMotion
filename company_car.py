import pygame
import random
from car import Car


class CompanyCar(Car):
    car_sprites = ("police", "taxi", "water_сarrier", "bus", "pickup")

    def __init__(self, x, y, width, height):
        Car.__init__(self, x, y, width, height)

        self._speed = random.randrange(2, 3)

        # img
        self._police_rotate_right = [pygame.image.load("img/sprites/police.png"),
                                     pygame.image.load("img/sprites/police-right.png")]

        self._taxi_rotate_right = [pygame.image.load("img/sprites/taxi.png"),
                                   pygame.image.load("img/sprites/taxi-right.png")]

        self._water_сarrier_rotate_right = [pygame.image.load("img/sprites/water_сarrier.png"),
                                            pygame.image.load("img/sprites/water_сarrier-right.png")]

        self._bus_rotate_right = [pygame.image.load("img/sprites/bus.png"),
                                  pygame.image.load("img/sprites/bus-right.png")]

        self._pickup_rotate_right = [pygame.image.load("img/sprites/pickup.png"),
                                     pygame.image.load("img/sprites/pickup-right.png")]
