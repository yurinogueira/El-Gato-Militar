import random
from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.model.ItemModel import ItemModel


class PowerUpModel(GameObjectInterface):
    def __init__(self):
        self.itemObject = ItemModel(POWER_UP_COIN)
        self.power = self.itemObject.item

        self.__setPosition_x = self.__random_x()
        self.__setPosition_y = random.randint(-50000, 0)
        self.power.set_position(self.__setPosition_x, self.__setPosition_y)


    def draw(self):
        self.power.draw()

    def update(self):
        self.power.update()

    def move(self, speed: int):
        self.power.y += speed * 5
        if self.power.y > HEIGHT_SCREEN + self.power.height and not self.itemObject.collided:
            self.power = ItemModel(POWER_UP_COIN).item
            self.power.set_position(self.__random_x(), random.randint(-50000, 0))

    def collide(self, obj):
        return self.itemObject.collide(obj)

    def generatesPoint(self, size):
        powers = []
        for i in range(size):
            powers.append(PowerUpModel())
        return powers

    def __random_x(self):
        return random.randint(0 + self.power.width, WIDTH_SCREEN - self.power.width)


