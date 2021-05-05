from PPlay.gameimage import GameImage
from constants import *
from src.factory.Text import CenterText


class Button:
    def __init__(self, window, x, y, text):
        self.window = window
        self.mouse = window.get_mouse()
        self.button = GameImage(NORMAL_BUTTON)
        self.button.set_position(x - self.button.width / 2, y - self.button.height / 2)
        self.is_normal = True
        self.is_button_press = False
        self.debug_time = 0
        self.x = x - self.button.width / 2
        self.y = y - self.button.height / 2
        self.text_str = text

    def draw(self):
        self.button.draw()
        color = NEAR_BLACK
        if self.mouse.is_over_object(self.button):
            color = ORANGE

        text = CenterText(self.window,
                          self.x + self.button.width / 2,
                          self.y + self.button.height / 2,
                          color=color,
                          size=80,
                          text=self.text_str)
        text.draw()
        self.update()

    def is_button_pressed(self):
        if self.is_button_press:
            self.is_button_press = False
            BUTTON_SOUND.play()
            return True
        return False

    def update(self):
        self.debug_time -= self.window.delta_time()
        if self.mouse.is_over_object(self.button):
            if not self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                self.button = GameImage(HOVER_BUTTON)
                self.button.set_position(self.x, self.y)
                self.is_normal = False
                self.is_button_press = False
            elif self.debug_time <= 0:
                self.debug_time = 1
                self.is_button_press = True
                self.is_normal = False
        elif not self.is_normal:
            self.button = GameImage(NORMAL_BUTTON)
            self.button.set_position(self.x, self.y)
            self.is_normal = True
            self.is_button_press = False


class ButtonClick(Button):
    def __init__(self, button_image, window, x, y):
        super().__init__(window, x, y, "")
        self.button = GameImage(button_image)
        self.button.set_position(x - self.button.width / 2, y - self.button.height / 2)

    def draw(self):
        self.button.draw()
        self.update()

    def is_button_pressed(self):
        if self.is_button_press:
            self.is_button_press = False
            BUTTON_SOUND.play()
            return True
        return False

    def update(self):
        self.debug_time -= self.window.delta_time()
        if self.mouse.is_over_object(self.button):
            if not self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                self.is_button_press = False
            elif self.debug_time <= 0:
                self.debug_time = 1
                self.is_button_press = True
