import pygame
import random
import math

display_width = 1300
display_height = 700

display = pygame.display.set_mode((display_width, display_height))


class Car:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self._width = width
        self._height = height

        self.x_start = x
        self.y_start = y

        self._angle = 0
        self.random_sprite()

        # Параметры для езды по кругу
        self._angle_of_rotation = 0
        self._counter_rotate = 0
        self._random_rotate = random.randrange(0, 4)

        self._counter_rotate_img = 0

    # Выбор рандомной машинки в классе
    def random_sprite(self):
        self._random_car = random.choice(self.car_sprites)
        self.car_sprite = pygame.image.load("img/sprites/" + self._random_car + ".png")
        self.car = self.car_sprite

        # Для поворотника
        self.car_copy = self.car

    # Движение машинок
    def draw(self):
        if self.x_start == 650 and self.y_start == 620:
            self.draw_down()
        elif self.x_start == 574 and self.y_start == 0:
            self.draw_up()
        elif self.x_start == 0 and self.y_start == 350:
            self.draw_left()
        elif self.x_start == 1220 and self.y_start == 270:
            self.draw_right()

    # Машинка едет снизу
    def draw_down(self):
        # Машинка едет по дороге
        if self.y >= -self._height:
            display.blit(self.car, (self.x, self.y))
            if self.y >= 540 and self._counter_rotate == 0:
                self.turn_signal_right()
                self.y -= self._speed
            # Поворот машинки на развязку в крайнюю правую полосу
            elif self._angle >= -68 and self._counter_rotate == 0:
                self._angle -= 1
                self.rotate(self._angle)
                self.rotate_img(self._angle)
                self.x += 0.5
                self.y -= 0.4
                self._angle_of_rotation = self._angle - 223  # начальная позиция машинки для вращения
                #  Проверка условия поворота
                if self._angle == -68:
                    self._counter_rotate += 1
                    self._angle = 140
            # Езда машинки по кругу + Рандомный съезд с круговой развязки
            # Cъезд вниз
            elif self._random_rotate == 0:
                if self._angle_of_rotation >= -610:
                    self.circle_movement(-610)
                # Выравнивание машинки
                elif self._angle > -500:
                    self._angle = -830
                # Поворот машинки направо с круговой развязки
                elif self._angle >= -899 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.y <= display_height and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, -180)
                    self.y += self._speed
                # Перерождение машикни
                else:
                    self.rebirth_car()

            # Съезд в право
            elif self._random_rotate == 1:
                if self._angle_of_rotation >= -340:
                    self.circle_movement(-340)
                # Выравнивание машинки
                elif self._angle >= 41:
                    self._angle = -381
                # Поворот машинки направо c круговой развязки
                elif self._angle >= -449 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y -= 0.4
                # Машинка уезжает
                elif self.x <= 1290 and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, -90)
                    self.x += self._speed
                # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд вверх
            elif self._random_rotate == 2:
                if self._angle_of_rotation >= -430:
                    self.circle_movement(-430)
                    # Выравнивание машинки
                elif self._angle >= -139:
                    self._angle = -290
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -359 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y -= 0.4
                    # Машинка уезжает
                elif self.y >= -75 and self._counter_rotate == 1:
                    self.y -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд влево
            elif self._random_rotate == 3:
                if self._angle_of_rotation >= -522:
                    self.circle_movement(-522)
                # Выравнивание машинки
                elif self._angle >= -323:
                    self._angle = -559
                # Поворот машинки направо c круговой развязки
                elif self._angle >= -629 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.x >= -self._width and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, 90)
                    self.x -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

    # Машинка едет сверху
    def draw_up(self):
        # Машинка едет по дороге
        if self.y <= display_height:
            display.blit(pygame.transform.rotate(self.car, 180), (self.x, self.y))
            if self.y <= 80 and self._counter_rotate == 0:
                self.turn_signal_right()
                self.y += self._speed
            # Поворот машинки на развязку в крайнюю правую полосу
            elif self._angle >= -68 and self._counter_rotate == 0:
                self._angle -= 1
                self.rotate(self._angle)
                self.rotate_img(self._angle)
                self.x -= 0.5
                self.y += 0.4
                self._angle_of_rotation = self._angle - 41  # начальная позиция машинки для вращения
                #  Проверка условия поворота
                if self._angle == -68:
                    self._counter_rotate += 1
                    self._angle = 140
            # Езда машинки по кругу + Рандомный съезд с круговой развязки
            # Cъезд вниз
            elif self._random_rotate == 0:
                if self._angle_of_rotation >= -250:
                    self.circle_movement(-250)
                # Выравнивание машинки
                elif self._angle > -144:
                    self._angle = -290
                # Поворот машинки направо с круговой развязки
                elif self._angle >= -359 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.y <= 690 and self._counter_rotate == 1:
                    self.y += self._speed
                # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд вправо
            elif self._random_rotate == 1:
                if self._angle_of_rotation >= -340:
                    self.circle_movement(-340)
                # Выравнивание машинки
                elif self._angle >= -323:
                    self._angle = -560
                # Поворот машинки направо c круговой развязки
                elif self._angle >= -629 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y -= 0.4
                # Машинка уезжает
                elif self.x <= 1290 and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, 90)
                    self.x += self._speed
                # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд вверх
            elif self._random_rotate == 2:
                if self._angle_of_rotation >= -430:
                    self.circle_movement(-430)
                    # Выравнивание машинки
                elif self._angle >= -503:
                    self._angle = -830
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -899 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y -= 0.4
                    # Машинка уезжает
                elif self.y >= -self._width * 2 and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, 180)
                    self.y -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд влево
            elif self._random_rotate == 3:
                if self._angle_of_rotation >= -160:
                    self.circle_movement(-160)
                    # Выравнивание машинки
                elif self._angle >= -37:
                    self._angle = -380
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -449 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.x >= -self._width and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, -90)
                    self.x -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

    # Машинка едет слева
    def draw_left(self):
        # Машинка едет по дороге
        if self.x <= display_width:
            display.blit(pygame.transform.rotate(self.car, -90), (self.x, self.y))
            if self.x <= 370 and self._counter_rotate == 0:
                self.turn_signal_right()
                self.x += self._speed
            # Поворот машинки на развязку в крайнюю правую полосу
            elif self._angle >= -68 and self._counter_rotate == 0:
                self._angle -= 1
                self.rotate(self._angle)
                self.rotate_img(self._angle)
                self.x += 0.5
                self.y += 0.4
                self._angle_of_rotation = self._angle - 130  # начальная позиция машинки для вращения
                #  Проверка условия поворота
                if self._angle == -68:
                    self._counter_rotate += 1
                    self._angle = 140
            # Езда машинки по кругу + Рандомный съезд с круговой развязки
            # Cъезд вниз
            elif self._random_rotate == 0:
                if self._angle_of_rotation >= -250:
                    self.circle_movement(-250)
                # Выравнивание машинки
                elif self._angle > -9:
                    self._angle = -17
                # Поворот машинки направо с круговой развязки
                elif self._angle >= -89 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.y <= display_height and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, -90)
                    self.y += self._speed
                # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд в право
            elif self._random_rotate == 1:
                if self._angle_of_rotation >= -340:
                    self.circle_movement(-340)
                # Выравнивание машинки
                elif self._angle >= -165:
                    self._angle = -288
                # Поворот машинки направо c круговой развязки
                elif self._angle >= -359 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y -= 0.4
                # Машинка уезжает
                elif self.x <= 1290 and self._counter_rotate == 1:
                    self.x += self._speed
                # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд вверх
            elif self._random_rotate == 2:
                if self._angle_of_rotation >= -429:
                    self.circle_movement(-429)
                    # Выравнивание машинки
                elif self._angle >= -347:
                    self._angle = -559
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -629 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y -= 0.4
                    # Машинка уезжает
                elif self.y >= -self._width * 2 and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, 90)
                    self.y -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд влево
            elif self._random_rotate == 3:
                if self._angle_of_rotation >= -522:
                    self.circle_movement(-522)
                    # Выравнивание машинки
                elif self._angle >= -529:
                    self._angle = -825
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -899 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.x >= -self._width and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, 180)
                    self.x -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

    # Машинка едет справа
    def draw_right(self):
        # Машинка едет по дороге
        if self.x >= -self._width:
            display.blit(pygame.transform.rotate(self.car, 90), (self.x, self.y))
            if self.x >= 850 and self._counter_rotate == 0:
                self.turn_signal_right()
                self.x -= self._speed
            elif self._angle >= -68 and self._counter_rotate == 0:
                self._angle -= 1
                self.rotate(self._angle)
                self.rotate_img(self._angle)
                self.x -= 0.5
                self.y -= 0.4
                self._angle_of_rotation = self._angle + 50
                # Проверка условия поворота
                if self._angle == -68:
                    self._counter_rotate += 1
                    self._angle = 140
            # Езда машикни по кругу + Рандомный съезд с круговой развязки
            # Съезд вниз
            elif self._random_rotate == 0:
                if self._angle_of_rotation >= -250:
                    self.circle_movement(-250)
                # Выравнивание машинки
                elif self._angle >= -375:
                    self._angle = -557
                # Поворот машинки направо с круговой развязки
                elif self._angle >= -629 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.y <= display_height and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, 90)
                    self.y += self._speed
                # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд вправо
            elif self._random_rotate == 1:
                if self._angle_of_rotation >= -340:
                    self.circle_movement(-340)
                # Выравнивание машинки
                elif self._angle >= -505:
                    self._angle = -828
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -899 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x += 0.5
                    self.y -= 0.4
                # Машинка уезжает
                elif self.x <= display_width and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, -180)
                    self.x += self._speed
                # Перерождение машинки
                else:
                    self.rebirth_car()

            # Cъезд вверх
            elif self._random_rotate == 2:
                if self._angle_of_rotation >= -70:
                    self.circle_movement(-70)
                    # Выравнивание машинки
                elif self._angle >= 35:
                    self._angle = -378
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -449 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y -= 0.4
                    # Машинка уезжает
                elif self.y >= -self._width * 2 and self._counter_rotate == 1:
                    self.car = pygame.transform.rotate(self.car_copy, -90)
                    self.y -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

            # Съезд влево
            elif self._random_rotate == 3:
                if self._angle_of_rotation >= -160:
                    self.circle_movement(-160)
                # Выравнивание машинки
                elif self._angle >= -145:
                    self._angle = -288
                    # Поворот машинки направо c круговой развязки
                elif self._angle >= -359 and self._counter_rotate == 1:
                    self._angle -= 1
                    self.rotate(self._angle)
                    self.rotate_img(self._angle)
                    self.x -= 0.5
                    self.y += 0.4
                # Машинка уезжает
                elif self.x >= -60 and self._counter_rotate == 1:
                    self.car = self.car_copy
                    self.x -= self._speed
                    # Перерождение машинки
                else:
                    self.rebirth_car()

    # Поворот направо
    def rotate(self, angle):
        orig_rect = self.car_sprite.get_rect()
        rot_image = pygame.transform.rotate(self.car_sprite, angle)
        rot_rect = self.car_sprite.get_rect()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()

        self.car = rot_image

    def rotate_img(self, angle):
        if self._counter_rotate_img == 50:
            self._counter_rotate_img = 0

        # SportCar
        elif self._random_car == "viper":
            orig_rect = self._viper_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._viper_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._viper_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "orange":
            orig_rect = self._orange_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._orange_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._orange_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "corvette":
            orig_rect = self._corvette_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._corvette_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._corvette_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "porsche":
            orig_rect = self._porsche_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._porsche_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._porsche_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "mercedes":
            orig_rect = self._mercedes_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._mercedes_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._mercedes_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        # CompanyCar
        elif self._random_car == "police":
            orig_rect = self._police_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._police_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._police_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "taxi":
            orig_rect = self._taxi_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._taxi_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._taxi_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "water_сarrier":
            orig_rect = self._water_сarrier_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._water_сarrier_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._water_сarrier_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "bus":
            orig_rect = self._bus_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._bus_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._bus_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "pickup":
            orig_rect = self._pickup_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._pickup_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._pickup_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        # PassengerCar
        elif self._random_car == "toyota":
            orig_rect = self._toyota_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._toyota_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._toyota_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "wish":
            orig_rect = self._wish_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._wish_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._wish_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "camry":
            orig_rect = self._camry_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._camry_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._camry_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "jeep":
            orig_rect = self._jeep_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._jeep_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._jeep_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        elif self._random_car == "audi":
            orig_rect = self._audi_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_image = pygame.transform.rotate(self._audi_rotate_right[self._counter_rotate_img // 25], angle)
            rot_rect = self._audi_rotate_right[self._counter_rotate_img // 25].get_rect()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()

            self.car = rot_image

        self._counter_rotate_img += 1

    # Движение по кругу
    def circle_movement(self, get_angle_of_rotation):
        if self._angle_of_rotation >= get_angle_of_rotation:
            angle = self._angle_of_rotation * 3.14 / 180

            self.x = 214 * math.cos(angle) + 610
            self.y = 214 * math.sin(angle) + 310

            self._angle_of_rotation -= 0.5  # здесь мы увеличиваем угол перемещения (скорость вращения по кругу)
            self._angle -= 1  # здесь мы увеличиваем угол поворота машинки во время езды по кругу

            self.rotate(-self._angle * 0.5)

    # Перерождение машины
    def rebirth_car(self):
        # Перерождение слева
        if self.y_start == 350 and self.x_start == 0:
            self.x = -80 - random.randrange(0, 1500)
            self.y = 350
            self._angle = 0
            self._counter_rotate = 0
            self._random_rotate = random.randrange(0, 4)
            self.random_sprite()
        # Перерождение справа
        elif self.y_start == 270 and self.x_start == 1220:
            self.x = 1220 + random.randrange(0, 1500)
            self.y = 270
            self._angle = 0
            self._counter_rotate = 0
            self._random_rotate = random.randrange(0, 4)
            self.random_sprite()
        # Перерождение снизу
        elif self.x_start == 650 and self.y_start == 620:
            self.x = 650
            self.y = 620 + random.randrange(0, 1500)
            self._angle = 0
            self._counter_rotate = 0
            self._random_rotate = random.randrange(0, 4)
            self.random_sprite()
        # Перрерождение сверху
        elif self.x_start == 574 and self.y_start == 0:
            self.x = 574
            self.y = -80 - random.randrange(0, 1500)
            self._angle = 0
            self._counter_rotate = 0
            self._random_rotate = random.randrange(0, 4)
            self.random_sprite()

    # Включение поворотника заранее
    def turn_signal_right(self):
        def turn_rotate(angle):
            # SportCar
            if self._random_car == "viper":
                display.blit(pygame.transform.rotate(self._viper_rotate_right[self._counter_rotate_img // 25], angle),
                             (self.x, self.y))

            elif self._random_car == "orange":
                display.blit(pygame.transform.rotate(self._orange_rotate_right[self._counter_rotate_img // 25], angle),
                             (self.x, self.y))

            elif self._random_car == "corvette":
                display.blit(
                    pygame.transform.rotate(self._corvette_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "porsche":
                display.blit(
                    pygame.transform.rotate(self._porsche_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "mercedes":
                display.blit(
                    pygame.transform.rotate(self._mercedes_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            # CompanyCar
            elif self._random_car == "police":
                display.blit(
                    pygame.transform.rotate(self._police_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "taxi":
                display.blit(
                    pygame.transform.rotate(self._taxi_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "water_сarrier":
                display.blit(
                    pygame.transform.rotate(self._water_сarrier_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "bus":
                display.blit(
                    pygame.transform.rotate(self._bus_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "pickup":
                display.blit(
                    pygame.transform.rotate(self._pickup_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            # PassengerCar
            elif self._random_car == "toyota":
                display.blit(
                    pygame.transform.rotate(self._toyota_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "wish":
                display.blit(
                    pygame.transform.rotate(self._wish_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "camry":
                display.blit(
                    pygame.transform.rotate(self._camry_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "jeep":
                display.blit(
                    pygame.transform.rotate(self._jeep_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

            elif self._random_car == "audi":
                display.blit(
                    pygame.transform.rotate(self._audi_rotate_right[self._counter_rotate_img // 25], angle),
                    (self.x, self.y))

        if self._counter_rotate_img >= 50:
            self._counter_rotate_img = 0

        elif 1100 >= self.x >= 850:
            turn_rotate(90)

        elif self.y >= 540:
            turn_rotate(0)

        elif self.y <= 80:
            turn_rotate(180)

        elif 130 <= self.x <= 370:
            turn_rotate(-90)

        self._counter_rotate_img += 1
