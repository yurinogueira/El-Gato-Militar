from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from constants import *


class LifeHud:
    def __init__(self, bar_x=4, bar_y=0, life_hud=LIFE_HUD, life_points=LIFE_POINTS):
        self.bar = GameImage(life_hud)
        self.bar.set_position(bar_x, bar_y)
        self.value = Sprite(*life_points)
        self.value.set_position(bar_x-10, bar_y-10)
        self.value.set_curr_frame(4)

    def draw(self):
        self.bar.draw()
        self.value.draw()

    def add_life(self):
        point = self.value.curr_frame + 1
        self.value.set_curr_frame(self.__checkLife(point))

    def full_life(self):
        self.value.set_curr_frame(4)

    def lose_life(self):
        point = self.value.curr_frame - 1
        if point >= 0:
            self.value.set_curr_frame(self.__checkLife(point))
        return point

    def is_empty_life(self):
        return self.value.curr_frame == 0

    def empty_life(self):
        self.value.set_curr_frame(0)

    def __checkLife(self, point):
        if point < 0:
            return 0
        elif point > 4:
            return 4
        else:
            return point

    def move(self, x, y):
        self.bar.set_position(x, y)
        self.value.set_position(x-10, y-10)


class EnemyLifeHud(LifeHud):
    def __init__(self, bar_x=4, bar_y=0, life_hud=LIFE_HUD, life_points=LIFE_POINTS):
        super().__init__(bar_x, bar_y, life_hud, life_points)
        self.value.set_position(bar_x-6, bar_y-3)
        self.is_hidden = False

    def move(self, x, y):
        self.bar.set_position(x, y)
        self.value.set_position(x-6, y-3)

    def draw(self):
        if not self.is_hidden:
            self.bar.draw()
            self.value.draw()

    def full_life(self):
        self.is_hidden = False
        self.value.set_curr_frame(4)

    def hidden(self):
        self.is_hidden = True
