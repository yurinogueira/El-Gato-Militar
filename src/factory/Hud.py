from src.hud.LifeHud import LifeHud
from src.hud.PointHud import PointHud
from src.hud.SpecialHud import SpecialHud
from src.hud.TimeHud import TimeHud
from src.hud.ShopHud import ShopHud
from src.hud.MenuHud import MenuHud

from constants import *


class HudManager:
    def __init__(self, window):
        self.window = window
        self.point = PointHud(window)
        self.time = TimeHud(window)
        self.shop = ShopHud(window)
        self.menu = MenuHud(window)
        self.life = LifeHud()
        self.special = SpecialHud()
        self.special_choose = FIRE_BALL_BLUE
        self.ship = JET_BLUE_FLY

    def get_ship_look(self) -> tuple:
        return self.ship

    def set_ship_look(self, animation: tuple):
        self.ship = animation

    def get_special_look(self) -> tuple:
        return self.special_choose

    def set_special_look(self, index: int) -> bool:
        if self.point.get_point() < 10:
            return False

        if index == 0:
            self.special_choose = FIRE_BALL_BLUE
        elif index == 1:
            self.special_choose = FIRE_BALL_PINK
        elif index == 2:
            self.special_choose = TORPEDO
        else:
            self.special_choose = TORPEDO_BLACK
        self.point.remove_point(10)
        return True

    def draw(self):
        self.__update()
        self.life.draw()
        self.special.draw()
        self.point.draw()
        self.shop.draw()
        self.menu.draw()

    def __update(self):
        self.menu.update()
        self.shop.update()

    def draw_with_time(self, state):
        self.draw()
        if state:
            self.time.draw()

    def add_points(self, amount):
        self.point.addPoint(amount)

    def add_life(self):
        self.life.add_life()

    def lose_life(self):
        self.life.lose_life()
        if self.life.is_empty_life():
            self.window.main_scene.change_scene('Over')

    def add_special(self):
        self.special.addSpecial()

    def lose_special(self):
        self.special.loseSpecial()

    def get_special(self):
        return self.special.current_special()

    def get_window(self):
        return self.window
