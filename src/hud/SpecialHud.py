from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite

from constants import *


class SpecialHud:
    def __init__(self):
        self.bar = GameImage(SPECIAL_HUD)
        self.bar.set_position(4, 76)
        self.value = Sprite(*SPECIAL_POINTS)
        self.value.set_position(-6, 65)
        self.value.set_curr_frame(0)

    def draw(self):
        self.bar.draw()
        self.value.draw()

    def addSpecial(self):
        point = self.value.curr_frame + 1
        self.value.set_curr_frame(self.__checkLife(point))

    def loseSpecial(self):
        self.value.set_curr_frame(0)

    def current_special(self):
        return self.value.curr_frame

    def __checkLife(self, point):
        if point < 0:
            return 0
        elif point > 4:
            return 4
        else:
            return point