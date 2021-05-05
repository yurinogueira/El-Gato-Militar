from PPlay.gameimage import GameImage
from constants import *
from src.factory.Button import Button


class MenuHud:
    def __init__(self, window):
        self.window = window
        self.button = GameImage(PAUSE_HUD)
        self.button.set_position(self.window.width - self.button.width - 10, self.window.height - 130)
        self.points = 0

        self.menu_screen = GameImage(PAUSE_SCREEN)
        self.menu_screen.set_position(self.window.width / 2 - self.menu_screen.width / 2, 85)

        self.menu_button = Button(self.window, self.window.width / 2, 320, "MENU")
        self.return_button = Button(self.window, self.window.width / 2, 500, "VOLTAR")

        self.show_menu = False

    def draw(self):
        self.button.draw()
        if self.show_menu:
            self.menu_screen.draw()
            self.menu_button.draw()
            self.return_button.draw()

    def update(self):
        if self.window.get_mouse().is_button_pressed(1) and self.window.get_mouse().is_over_object(self.button):
            BUTTON_SOUND.play()
            self.window.main_scene.running = False
            self.show_menu = True
        elif self.window.get_keyboard().key_pressed("ESCAPE") or self.return_button.is_button_pressed():
            self.window.main_scene.running = True
            self.show_menu = False
        elif self.menu_button.is_button_pressed():
            self.window.main_scene.running = True
            self.show_menu = False
            self.window.main_scene.change_scene()
