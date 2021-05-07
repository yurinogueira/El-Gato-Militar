from PPlay.gameimage import GameImage

from src.factory.Text import CenterText

from constants import *


class PointHud:

    def __init__(self, window):
        self.window = window
        self.bar = GameImage(POINTS_HUD)
        self.bar.set_position(self.window.width - self.bar.width, 0)
        self.points = 0

    def draw(self):
        self.bar.draw()
        text = CenterText(self.window, self.window.width - self.bar.width / 2 - 8, 40, text=self.points)
        text.draw()

    def addPoint(self, amount):
        self.points += amount

    def get_point(self):
        return self.points

    def remove_point(self, amount: int):
        self.points -= amount