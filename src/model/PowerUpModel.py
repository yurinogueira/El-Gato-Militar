from PPlay.sprite import Sprite
from src.factory.Points import Point
import constants as const
import random


class PowerUpModel:
    def __init__(self):
        self.animation = Sprite(*const.POWER_UP_COIN)
        self.animation.set_total_duration(1000)
        self.animation.set_position(random.randint(0+self.animation.width, const.WIDTH_SCREEN-self.animation.width), random.randint(-1550, 0))
        self.x = self.animation.x
        self.y = self.animation.y

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
        return 1

    def move(self):
        self.animation.y += 0.2

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()
