from PPlay.gameimage import GameImage

from src.factory.Button import Button
from src.factory.Hud import HudManager
from src.factory.Text import CenterText

from constants import *
from src.interfaces.SceneInteface import SceneInterface


class HistoryScene(SceneInterface):
    def __init__(self, hud: HudManager, imageHistory, nextScene):
        self.hud = hud
        self.window = hud.get_window()
        self.fundo = GameImage(imageHistory)
        self.nextScene = nextScene

        self.button_continuar = Button(self.window, WINDOW_SIZE[0] - 200, WINDOW_SIZE[1] - 100, "CERTO!")

    def handle_event(self, speed: int, scene: bool):
        pass
    def draw(self, state: bool):
        self.fundo.draw()
        self.button_continuar.draw()
    def update(self, state: bool):
        if self.button_continuar.is_button_pressed():
            self.window.main_scene.change_scene(self.nextScene)
