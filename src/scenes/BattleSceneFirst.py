from constants import *
from src.factory.Hud import HudManager
from src.interfaces.SceneInteface import SceneInterface
from src.model.AirPlaneModel import AirPlaneModel
from src.model.BackgroundModel import BackgroundModel


class BattleSceneFirst(SceneInterface):
    def __init__(self, hud):
        self.hud = hud
        self.background = BackgroundModel(BACKGROUND_BATTLE1)
        self.airplane = AirPlaneModel()
        self.fps = 0

    def handle_event(self, speed, event):
        self.fps = speed
        if event.key_pressed("UP"):  # Direcional ^
            self.airplane.up(self.fps)
        if event.key_pressed("DOWN"):
            self.airplane.down(self.fps)
        if event.key_pressed("RIGHT"):
            self.airplane.forward(self.fps)
        if event.key_pressed("LEFT"):
            self.airplane.backward(self.fps)

        self.background.move(self.fps)
        self.airplane.move(self.fps)

    def draw(self):
        self.background.draw()
        self.airplane.draw()
        self.hud.draw()

    def update(self):
        self.background.update()
        self.airplane.update()
