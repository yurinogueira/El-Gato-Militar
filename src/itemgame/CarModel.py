import random
from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ItemModel import ItemModel


class CarModel(GameObjectInterface):
    def __init__(self, x, carImage=CAR_1, reverse=False):
        self.car = ItemModel(carImage)
        self.carAnimation = self.car.animation
        self.x = x

        if reverse:
            self.carAnimation.set_position(WIDTH_SCREEN + self.x,
                                           HEIGHT_SCREEN - self.carAnimation.height - 100)
        else:
            self.carAnimation.set_position(WIDTH_SCREEN - self.x, HEIGHT_SCREEN - self.carAnimation.height - 30)

        self.movimentation = reverse

    def draw(self):
        self.carAnimation.draw()

    def update(self):
        self.carAnimation.update()

    def move(self, fps: int):
        if self.movimentation:
            self.carAnimation.x -= fps * 1.7
            if self.carAnimation.x + self.carAnimation.width < 0:
                self.carAnimation.set_position(WIDTH_SCREEN + self.x,
                                               HEIGHT_SCREEN - self.carAnimation.height - 100)

        else:
            self.carAnimation.x += fps
            if self.carAnimation.x > WIDTH_SCREEN:
                self.carAnimation.set_position(- self.x, HEIGHT_SCREEN - self.carAnimation.height - 30)
