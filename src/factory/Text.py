import pygame

from constants import *


class CenterText:
    def __init__(self, window, x, y, color=WHITE, size=64, text=""):
        self.window = window
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.textStr = str(text)

        self.font = pygame.font.SysFont("Arial", int(self.size * 0.7), bold=False, italic=False)
        self.text = self.font.render(self.textStr, True, self.color)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def draw(self):
        self.window.screen.blit(self.text, self.text_rect)

    def update_position(self, x, y):
        self.__update(x=x, y=y)

    def update_color(self, color):
        self.__update(color=color)

    def update_size(self, size):
        self.__update(size=size)

    def update_text(self, text):
        self.__update(text=str(text))

    def __update(self, x=None, y=None, color=None, size=None, text=None):
        self.x = self.x if x is None else x
        self.y = self.y if y is None else y
        self.color = self.color if color is None else color
        self.size = self.size if size is None else size
        self.textStr = self.textStr if text is None else text

        self.text = pygame.font.Font(None, self.size).render(self.textStr, True, self.color)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))
