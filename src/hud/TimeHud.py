from pplay.gameimage import GameImage
from pplay.text import Text

from constants import *


class TimeHud:

    def __init__(self, window):
        self.window = window
        self.bar = GameImage(TIME_HUD)
        self.bar.set_position(self.window.width / 2 - self.bar.width / 2, 6)
        self.time = TIME

    def draw(self):
        self.bar.draw()
        self.time = self.time - self.window.delta_time()
        seconds = self.time

        if int(seconds) == 0:
            self.window.main_scene.change_scene('City')

        text = Text(self.window.width / 2, 46, text=int(seconds))
        text.draw()
