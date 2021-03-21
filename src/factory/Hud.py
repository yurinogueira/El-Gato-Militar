from src.hud.LifeHud import LifeHud
from src.hud.PointHud import PointHud
from src.hud.SpecialHud import SpecialHud
from src.hud.TimeHud import TimeHud
from src.hud.ShopHud import ShopHud
from src.hud.MenuHud import MenuHud


class HudManager:
    def __init__(self, window):
        self.point = PointHud(window)
        self.time = TimeHud(window)
        self.shop = ShopHud(window)
        self.menu = MenuHud(window)
        self.life = LifeHud()
        self.special = SpecialHud()

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
        self.life.addLife()

    def lose_life(self):
        self.life.loseLife()

    def add_special(self):
        self.special.addSpecial()

    def lose_special(self):
        self.special.loseSpecial()
