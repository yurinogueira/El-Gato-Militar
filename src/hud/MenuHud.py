from PPlay.gameimage import GameImage
from constants import *
from src.factory.Text import CenterText


show_menu = False


def change_show_menu(value):
    global show_menu
    show_menu = value


class MenuHud:
    def __init__(self, window):
        self.window = window
        self.button = GameImage(PAUSE_HUD)
        self.button.set_position(self.window.width - self.button.width - 10, self.window.height - 130)
        self.points = 0

        self.menu_screen = GameImage(PAUSE_SCREEN)
        self.menu_screen.set_position(self.window.width / 2 - self.menu_screen.width / 2, 85)

        self.menu_button = Button(self.window, 240, True)
        self.return_button = Button(self.window, 420, False)

    def draw(self):
        self.button.draw()
        if show_menu:
            self.menu_screen.draw()
            self.menu_button.draw()
            self.return_button.draw()

    def update(self):
        import teste
        if self.window.get_mouse().is_button_pressed(1) and self.window.get_mouse().is_over_object(self.button):
            teste.change_state(False)
            change_show_menu(True)
        if self.window.get_keyboard().key_pressed("ESCAPE"):
            teste.change_state(True)
            change_show_menu(False)


class Button:
    def __init__(self, window, y, is_menu):
        self.window = window
        self.mouse = window.get_mouse()
        self.is_menu = is_menu
        self.button = GameImage(NORMAL_BUTTON)
        self.button.set_position(self.window.width / 2 - self.button.width / 2, y)
        self.x = self.window.width / 2 - self.button.width / 2
        self.y = y
        self.is_normal = True

    def draw(self):
        self.button.draw()
        text_str = "VOLTAR"
        if self.is_menu:
            text_str = "MENU"

        text = CenterText(self.window,
                          self.window.width / 2,
                          self.y + self.button.height / 2,
                          color=NEAR_BLACK,
                          size=80,
                          text=text_str)
        if self.mouse.is_over_object(self.button):
            text = CenterText(self.window,
                              self.window.width / 2,
                              self.y + self.button.height / 2,
                              color=ORANGE,
                              size=80,
                              text=text_str)
        text.draw()
        self.update()

    def update(self):
        if self.mouse.is_over_object(self.button):
            if self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                import teste
                if self.is_menu:
                    teste.change_state(True)
                    change_show_menu(False)
                    teste.change_scene('Main')
                else:
                    change_show_menu(False)
                    teste.change_state(True)
            elif self.is_normal:
                self.button = GameImage(HOVER_BUTTON)
                self.button.set_position(self.x, self.y)
                self.is_normal = False
        elif not self.is_normal:
            self.button = GameImage(NORMAL_BUTTON)
            self.button.set_position(self.x, self.y)
            self.is_normal = True
