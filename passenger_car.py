import pygame
import random
from car import Car


class PassengerCar(Car):
    car_sprites = ("toyota", "wish", "camry", "jeep", "audi")

    def __init__(self, x, y, width, height):
        Car.__init__(self, x, y, width, height)

        self._speed = random.randrange(3, 4)

        # img right
        self._toyota_rotate_right = [pygame.image.load("img/sprites/toyota.png"),
                                     pygame.image.load("img/sprites/toyota-right.png")]

        self._wish_rotate_right = [pygame.image.load("img/sprites/wish.png"),
                                   pygame.image.load("img/sprites/wish-right.png")]

        self._camry_rotate_right = [pygame.image.load("img/sprites/camry.png"),
                                    pygame.image.load("img/sprites/camry-right.png")]

        self._jeep_rotate_right = [pygame.image.load("img/sprites/jeep.png"),
                                   pygame.image.load("img/sprites/jeep-right.png")]

        self._audi_rotate_right = [pygame.image.load("img/sprites/audi.png"),
                                   pygame.image.load("img/sprites/audi-right.png")]
