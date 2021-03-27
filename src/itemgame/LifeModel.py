from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ItemModel import ItemModel
from src.model.AirPlaneModel import AirPlaneModel


class LifeModel(GameObjectInterface):
    def __init__(self, x: int, y: int, movimentation: bool):
        self.life = ItemModel(POWER_UP_LIFE)
        self.lifeAnimation = self.life.animation

        self.original_x = x
        self.original_y = y
        self.lifeAnimation.set_position(x, y)
        self.visible = movimentation
        self.module = -1
        self.direction = 3

    def draw(self):
        self.lifeAnimation.draw()

    def update(self):
        self.lifeAnimation.update()

    def move(self, fps: int):
        amplitude = 100
        if self.visible:

            if self.lifeAnimation.y < self.original_y - amplitude:
                self.lifeAnimation.y = self.original_y - amplitude
                self.direction *= self.module
            elif self.lifeAnimation.y > self.original_y + amplitude:
                self.lifeAnimation.y = self.original_y + amplitude
                self.direction *= self.module

            self.lifeAnimation.y -= (fps / 2) * self.direction
            self.lifeAnimation.x -= (fps / 4) * 5

    def collide(self, obj):
        return self.life.collide(obj)

    def change_visibility(self, x=2000, y=2000):
        self.life.animation.set_position(x, y)
        self.visible = not self.visible