from constants import *
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
        self.bar_time.set_position(self.window.width / 2 - self.bar_time.width / 2, 0)

    def add_points(self, amount):
        self.points += amount

    def set_time(self, time):
        self.time = time

    def points_hud(self):
        self.bar_points.draw()
        text = CenterText(self.window, self.window.width - self.bar_points.width / 2 - 16, 64, text=self.points)
        text.draw()

    def time_hud(self, scene_name):
        self.bar_time.draw()
        seconds = self.time - (self.window.time_elapsed() / 1000) % 60

        if seconds == 0:
            import teste
            teste.change_scene(scene_name)

        text = CenterText(self.window, self.window.width / 2, 58, text=int(seconds))
        text.draw()
