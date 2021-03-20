from PPlay.gameimage import GameImage
from constants import *
from src.factory.Text import CenterText


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


