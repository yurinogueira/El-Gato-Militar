from PPlay.gameimage import GameImage
from src.factory.Button import Button
from src.factory.Hud import HudManager
from src.factory.Text import CenterText
from src.interfaces.SceneInteface import SceneInterface

from constants import *


class GameOverScene(SceneInterface):
    def __init__(self, hud: HudManager):
        self.hud = hud
        self.window = hud.get_window()
        self.background = GameImage(BACKGROUND_HOME)
        self.text = CenterText(self.window, self.window.width / 2, 50, WHITE, text="Você perdeu!")

        self.voltar_button = Button(self.window, self.window.width / 2, self.window.height / 2, "VOLTAR")

    def handle_event(self, fps, state):
        if self.voltar_button.is_button_pressed():
            self.window.main_scene.change_scene('Main')

    def draw(self, state):
        self.background.draw()
        self.text.draw()
        self.voltar_button.draw()

    def update(self, state):
        self.voltar_button.update()
