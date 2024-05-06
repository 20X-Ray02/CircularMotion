import pygame
import random
from car import Car


class SportCar(Car):
    car_sprites = ("viper", "orange", "corvette", "porsche", "mercedes")

    def __init__(self, x, y, width, height):
        Car.__init__(self, x, y, width, height)

        self._speed = random.randrange(4, 6)

        # img
        self._viper_rotate_right = [pygame.image.load("img/sprites/viper.png"),
                                    pygame.image.load("img/sprites/viper-right.png")]

        self._orange_rotate_right = [pygame.image.load("img/sprites/orange.png"),
                                     pygame.image.load("img/sprites/orange-right.png")]

        self._corvette_rotate_right = [pygame.image.load("img/sprites/corvette.png"),
                                       pygame.image.load("img/sprites/corvette-right.png")]

        self._porsche_rotate_right = [pygame.image.load("img/sprites/porsche.png"),
                                      pygame.image.load("img/sprites/porsche-right.png")]

        self._mercedes_rotate_right = [pygame.image.load("img/sprites/mercedes.png"),
                                       pygame.image.load("img/sprites/mercedes-right.png")]
