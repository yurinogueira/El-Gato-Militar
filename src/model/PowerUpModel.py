from PPlay.sprite import Sprite
from src.factory.Points import Point
import constants as const
import random


class PowerUpModel:
    def __init__(self):
        self.__coinValue = 0
        self.animation = self.__coinsImg()
        self.animation.set_total_duration(1000)
        self.__setPosition_x = self.__random_x()
        self.__setPosition_y = random.randint(-50000, 0)
        self.animation.set_position(self.__setPosition_x, self.__setPosition_y)
        self.x = self.animation.x
        self.y = self.animation.y
        self.collided = False

    def collide(self, obj):
        l2 = Point(self.animation.x, self.animation.y)
        r2 = Point(self.animation.x + self.animation.width, self.animation.y + self.animation.height)

        l1 = Point(obj.animation.x + (obj.animation.width * 0.2),
                   obj.animation.y + (obj.animation.height * 0.12))
        r1 = Point(obj.animation.x + obj.animation.width - (obj.animation.width * 0.32),
                   obj.animation.y + obj.animation.height - (obj.animation.height * 0.1))

        if r1.x < l2.x or r2.x < l1.x:
            return 0

        if r1.y < l2.y or r2.y < l1.y:
            return 0

        self.animation.set_position(2000, 2000)
        self.collided = True
        return self.__coinValue

    def move(self, speed):
        self.animation.y += speed * 5
        if self.animation.y > const.HEIGHT_SCREEN + self.animation.height and not self.collided:
            self.animation = self.__coinsImg()
            self.animation.set_total_duration(1000)
            self.animation.set_position(self.__random_x(), random.randint(-50000, 0))

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()

    def __random_x(self):
        return random.randint(0 + self.animation.width, const.WIDTH_SCREEN - self.animation.width)

    def __coinsImg(self):
        damage = random.randint(0, 11) % 5
        if damage == 0:
            self.__coinValue = -1
            return Sprite(*const.POWER_UP_DAMAGE)
        else:
            self.__coinValue = 1
            return Sprite(*const.POWER_UP_COIN)
