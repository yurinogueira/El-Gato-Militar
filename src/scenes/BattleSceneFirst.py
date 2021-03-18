from PPlay.gameimage import *
from constants import *
from src.model.AirPlaneModel import AirPlaneModel


class BattleSceneFirst:
    def __init__(self, hud):
        self.hud = hud
        self.fundo = GameImage(BACKGROUND_BATTLE1)
        self.airplane = AirPlaneModel()
        self.speed = 0
        self.fps = 5

    def handle_event(self, speed, event):
        self.speed = speed
        if event.key_pressed("UP"):  # Direcional ^
            self.airplane.up(self.fps)
        elif event.key_pressed("DOWN"):
            self.airplane.down(self.fps)
        elif event.key_pressed("RIGHT"):
            self.airplane.forward(self.fps)
        elif event.key_pressed("LEFT"):
            self.airplane.backward(self.fps)

    def draw(self):
        self.fundo.draw()
        self.airplane.draw()
        self.hud.points_hud()

    def update(self):
        self.airplane.move(self.speed)
        self.airplane.update()
