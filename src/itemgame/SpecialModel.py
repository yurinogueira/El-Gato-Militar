import random

from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ItemModel import ItemModel


class SpecialModel (GameObjectInterface):
    def __init__(self, x: int, y: int, movimentation: bool):
        self.special = ItemModel(POWER_UP_ENERGY)
        self.special_animation = self.special.animation

        self.original_x = x
        self.original_y = y
        self.special_animation.set_position(x, y)
        self.movimentation = movimentation
        self.module = -1
        self.direction = 3
        self.time = 0

    def draw(self):
        self.special_animation.draw()

    def update(self):
        self.special_animation.update()

    def move(self, fps: int):
        if self.movimentation:
            self.time += 1
            if self.time % 25 == 0:
                start_x = self.original_x - 250
                start_y = self.original_y - 250
                end_x = self.original_x + 250
                end_y = self.original_y + 250
                self.special.animation.set_position(
                    random.randint(start_x, end_x),
                    random.randint(start_y, end_y)
                )
                self.time = 0


    def collide(self, obj):
        return self.special.collide(obj)

    def disable_movimentation(self):
        self.movimentation = False
