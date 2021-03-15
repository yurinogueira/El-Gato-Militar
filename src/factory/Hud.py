from constants import *
from PPlay.sprite import Sprite
from PPlay.gameimage import GameImage
from src.factory.Text import CenterText


class HudManager:
    def __init__(self, window):
        self.window = window
        self.points = 0
        self.time = 0

        self.bar_points = GameImage(POINTS_HUD)
        self.bar_points.set_position(self.window.width - self.bar_points.width, 0)

        self.bar_time = GameImage(TIME_HUD)
        self.bar_time.set_position(self.window.width / 2 - self.bar_time.width / 2, 6)

        self.bar_life = GameImage(LIFE_HUD)
        self.bar_life.set_position(4, 0)
        self.life_value = Sprite(*LIFE_POINTS)
        self.life_value.set_position(-6, -10)

        self.bar_special = GameImage(SPECIAL_HUD)
        self.bar_special.set_position(4, 76)
        self.special_value = Sprite(*SPECIAL_POINTS)
        self.special_value.set_position(-6, 65)

    def add_points(self, amount):
        self.points += amount

    def set_time(self, time):
        self.time = time

    def points_hud(self):
        self.bar_points.draw()
        text = CenterText(self.window, self.window.width - self.bar_points.width / 2 - 8, 40, text=self.points)
        text.draw()

    def time_hud(self, scene_name):
        self.bar_time.draw()
        seconds = self.time - (self.window.time_elapsed() / 1000) % 60

        if seconds == 0:
            import teste
            teste.change_scene(scene_name)

        text = CenterText(self.window, self.window.width / 2, 46, text=int(seconds))
        text.draw()

    def life_hud(self, amount=3):
        self.bar_life.draw()
        self.life_value.set_curr_frame(amount - 1)
        self.life_value.draw()

    def special_hud(self, amount=3):
        self.bar_special.draw()
        self.special_value.set_curr_frame(amount - 1)
        self.special_value.draw()
