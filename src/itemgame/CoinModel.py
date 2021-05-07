import random

from src.interfaces.GameObjectInterface import GameObjectInterface

from src.itemgame.ItemModel import ItemModel

from constants import *


class CoinModel(GameObjectInterface):
    def __init__(self, x=0, y=0, movimentation=True):
        self.coin = ItemModel(POWER_UP_COIN)
        self.coinAnimation = self.coin.animation

        self.coinAnimation.set_position(x, y)
        self.movimentation = movimentation

    def draw(self):
        self.coinAnimation.draw()

    def update(self):
        self.coinAnimation.update()

    def move(self, fps: int):
        if self.movimentation:
            self.coinAnimation.y += (fps/5) * 5
            if self.coinAnimation.y > HEIGHT_SCREEN + self.coinAnimation.height and not self.coin.collided:
                self.coin = ItemModel(POWER_UP_COIN)
                self.coinAnimation = self.coin.animation
                self.coinAnimation.set_position(self.__random_x(), random.randint(-5000, 0))

    def collide(self, obj):
        if self.coin.collide(obj):
            self.coinAnimation.set_position(self.__random_x(), -2500)
            COIN_SOUND.play()
            return True
        return False

    def generatesPoint(self, size):
        powers = []
        for i in range(size):
            powers.append(CoinModel(self.__random_x(), random.randint(-5000, 0), True))
        return powers

    def __random_x(self):
        return random.randint(0 + self.coinAnimation.width, WIDTH_SCREEN - self.coinAnimation.width)


