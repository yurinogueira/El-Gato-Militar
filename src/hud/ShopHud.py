from PPlay.gameimage import GameImage
from constants import *


class ShopHud:

    def __init__(self, window):
        self.window = window
        self.mouse = window.get_mouse()
        self.button = GameImage(SHOP_HUD)
        self.button.set_position(10, self.window.height - 130)
        self.points = 0

    def draw(self):
        self.button.draw()

    def update(self):
        if self.mouse.is_over_object(self.button) and self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
            # faz alguma coisa ai meu
            print("CADE O SHOP")