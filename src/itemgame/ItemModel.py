

from PPlay.sprite import Sprite
from constants import *
from src.factory.Point import Point


class ItemModel:
    def __init__(self, *sprite):
        self.animation = Sprite(*sprite[0])
        self.animation.set_total_duration(1000)
        self.__setPosition_x = 0
        self.__setPosition_y = 0
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
            return False

        if r1.y < l2.y or r2.y < l1.y:
            return False

        self.animation.set_position(2000, 2000)
        self.collided = True
        return self.collided
