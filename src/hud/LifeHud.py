from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface


class LifeHud():

    def __init__(self):
        self.bar = GameImage(LIFE_HUD)
        self.bar.set_position(4, 0)
        self.value = Sprite(*LIFE_POINTS)
        self.value.set_position(-6, -10)
        self.value.set_curr_frame(1)


    def draw(self):
        self.bar.draw()
        self.value.draw()

    def addLife(self):
        point = self.value.curr_frame + 1
        self.value.set_curr_frame(self.__checkLife(point))

    def loseLife(self):
        point = self.value.curr_frame - 1
        self.value.set_curr_frame(self.__checkLife(point))

    def __checkLife(self, point):
        if point < 0:
            return 0
        elif point > 2:
            return 2
        else:
            return point