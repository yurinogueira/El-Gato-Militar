from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface


class SpecialHud():

    def __init__(self):
        self.bar = GameImage(SPECIAL_HUD)
        self.bar.set_position(4, 76)
        self.value = Sprite(*SPECIAL_POINTS)
        self.value.set_position(-6, 65)
        self.value.set_curr_frame(1)

    def draw(self):
        self.bar.draw()
        self.value.draw()

    def addSpecial(self):
        point = self.value.curr_frame + 1
        self.value.set_curr_frame(self.__checkLife(point))

    def loseSpecial(self):
        point = self.value.curr_frame - 1
        self.value.set_curr_frame(self.__checkLife(point))

    def __checkLife(self, point):
        if point < 0:
            return 0
        elif point > 2:
            return 2
        else:
            return point