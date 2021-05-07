from PPlay.gameimage import GameImage
from constants import *
from src.factory.Button import Button
from src.factory.Hud import HudManager
from src.interfaces.SceneInteface import SceneInterface


class HistoryScene(SceneInterface):
    def __init__(self, hud: HudManager, imageHistory, nextScene, continue_game = True):
        self.hud = hud
        self.window = hud.get_window()
        self.fundo = GameImage(imageHistory)
        self.nextScene = nextScene
        self.continue_game = continue_game

        if self.continue_game:
            self.button_continuar = Button(self.window, WINDOW_SIZE[0] - 200, WINDOW_SIZE[1] - 100, "CERTO!")

    def handle_event(self, speed: int, scene: bool):
        pass
    def draw(self, state: bool):
        self.fundo.draw()
        if self.continue_game:
            self.button_continuar.draw()
    def update(self, state: bool):
        if self.continue_game:
            if self.button_continuar.is_button_pressed():
                self.window.main_scene.change_scene(self.nextScene)
