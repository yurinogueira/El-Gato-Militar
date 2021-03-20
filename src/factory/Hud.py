from src.hud.LifeHud import LifeHud
from src.hud.PointHud import PointHud
from src.hud.SpecialHud import SpecialHud
from src.hud.TimeHud import TimeHud


class HudManager:
    def __init__(self, window):
        self.point = PointHud(window)
        self.time = TimeHud(window)
        self.life = LifeHud()
        self.special = SpecialHud()

    def draw(self):
        self.life.draw()
        self.special.draw()
        self.point.draw()

    def draw_with_time(self):
        self.draw()
        self.time.draw()

    def add_points(self, amount):
        self.point.addPoint(amount)

    def set_time(self, time):
        self.time.setTime(time)

    def add_life(self):
        self.life.addLife()

    def lose_life(self):
        self.life.loseLife()

    def add_special(self):
        self.special.addSpecial()

    def lose_special(self):
        self.special.loseSpecial()
