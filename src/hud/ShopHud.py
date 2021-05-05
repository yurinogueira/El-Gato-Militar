from PPlay.gameimage import GameImage

from constants import *

from src.factory.Text import CenterText


class ShopHud:
    def __init__(self, window):
        self.window = window
        self.mouse = window.get_mouse()

        self.button = GameImage(SHOP_HUD)
        self.button.set_position(10, self.window.height - 130)

        self.shop_screen = GameImage(SHOP_SCREEN)
        self.shop_screen.set_position(self.window.width / 2 - self.shop_screen.width / 2, 85)

        self.blue_fire_shop = GameImage(BLUE_FIRE_SHOP)
        self.blue_fire_shop.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.blue_fire_shop_b = GameImage(BLUE_FIRE_SHOP_B)
        self.blue_fire_shop_b.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.blue_text = CenterText(self.window, self.window.width / 2 + 20, 294, color=SKY_BLUE, size=46, text="10 C")

        self.pink_fire_shop = GameImage(PINK_FIRE_SHOP)
        self.pink_fire_shop.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.pink_fire_shop_b = GameImage(PINK_FIRE_SHOP_B)
        self.pink_fire_shop_b.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.pink_text = CenterText(self.window, self.window.width / 2 + 20, 370, color=PURPLE, size=46, text="10 C")

        self.torpedo_shop = GameImage(TORPEDO_SHOP)
        self.torpedo_shop.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.torpedo_shop_b = GameImage(TORPEDO_SHOP_B)
        self.torpedo_shop_b.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.torpedo_text = CenterText(self.window, self.window.width / 2 + 20, 446, color=FOREST_GREEN, size=46, text="10 C")

        self.torpedo_black_shop = GameImage(TORPEDO_BLACK_SHOP)
        self.torpedo_black_shop.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.torpedo_black_shop_b = GameImage(TORPEDO_BLACK_SHOP_B)
        self.torpedo_black_shop_b.set_position(self.window.width / 2 - self.shop_screen.width / 2, 140)
        self.torpedo_black_text = CenterText(self.window, self.window.width / 2 + 20, 522, color=BLACK, size=46, text="10 C")

        self.choose_skin = [True, False, False, False]

        self.points = 0
        self.show_shop = False

    def draw_shop(self):
        if self.choose_skin[0]:
            self.blue_fire_shop_b.draw()
            self.pink_fire_shop.draw()
            self.torpedo_shop.draw()
            self.torpedo_black_shop.draw()
        elif self.choose_skin[1]:
            self.blue_fire_shop.draw()
            self.pink_fire_shop_b.draw()
            self.torpedo_shop.draw()
            self.torpedo_black_shop.draw()
        elif self.choose_skin[2]:
            self.blue_fire_shop.draw()
            self.pink_fire_shop.draw()
            self.torpedo_shop_b.draw()
            self.torpedo_black_shop.draw()
        elif self.choose_skin[3]:
            self.blue_fire_shop.draw()
            self.pink_fire_shop.draw()
            self.torpedo_shop.draw()
            self.torpedo_black_shop_b.draw()
        self.blue_text.draw()
        self.pink_text.draw()
        self.torpedo_text.draw()
        self.torpedo_black_text.draw()

    def draw(self):
        self.button.draw()
        if self.show_shop:
            self.shop_screen.draw()
            self.draw_shop()

    def update(self):
        if self.__is_clicking(self.button):
            BUTTON_SOUND.play()
            self.window.main_scene.running = False
            self.show_shop = True
        elif self.window.get_keyboard().key_pressed("ESCAPE"):
            self.window.main_scene.running = True
            self.show_shop = False
        elif self.__is_clicking_shop(0):
            if self.window.main_scene.get_hud().set_special_look(0):
                self.choose_skin = [True, False, False, False]
        elif self.__is_clicking_shop(1):
            if self.window.main_scene.get_hud().set_special_look(1):
                self.choose_skin = [False, True, False, False]
        elif self.__is_clicking_shop(2):
            if self.window.main_scene.get_hud().set_special_look(2):
                self.choose_skin = [False, False, True, False]
        elif self.__is_clicking_shop(3):
            if self.window.main_scene.get_hud().set_special_look(3):
                self.choose_skin = [False, False, False, True]

    def __is_clicking(self, button: GameImage):
        return self.mouse.is_over_object(button) and self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT)

    def __is_clicking_shop(self, pos: int):
        if self.choose_skin[pos]:
            return False
        if pos == 0:
            if self.mouse.is_over_area((480, 250), (800, 330)) and self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                return True
        elif pos == 1:
            if self.mouse.is_over_area((480, 331), (800, 410)) and self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                return True
        elif pos == 2:
            if self.mouse.is_over_area((480, 411), (800, 480)) and self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                return True
        else:
            if self.mouse.is_over_area((480, 481), (800, 560)) and self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                return True
        return False
