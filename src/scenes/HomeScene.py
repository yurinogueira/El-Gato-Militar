from PPlay.gameimage import *
from constants import *
from src.interfaces.SceneInteface import SceneInterface
from src.model.CatModel import CatModel
from src.model.PowerUpModel import PowerUpModel


class HomeScene(SceneInterface):

    def __init__(self, hud):
        self.hud = hud
        self.fundo = GameImage(BACKGROUND_HOME)
        self.cat = CatModel()
        self.speed = 0
        self.power = PowerUpModel()
        self.listPower = self.power.generatesPoint(60)
        self.temp_points = 0

    def handle_event(self, speed, event, state):
        if not state:
            return

        self.speed = speed
        if event.key_pressed("UP"):  # Direcional ^
            self.cat.jump(300)
        elif event.key_pressed("LEFT"):
            self.cat.walk_fliped()
        elif event.key_pressed("RIGHT"):
            self.cat.walk()
        else:
            self.cat.idle()

        for p in self.listPower:
            p.move(self.speed)
            if p.collide(self.cat):
                self.temp_points += 1

    def draw(self, state):
        if state:
            self.fundo.draw()
            for p in self.listPower:
                p.draw()

            self.cat.draw()

        self.hud.draw_with_time(state)

    def update(self, state):
        if not state:
            return

        self.hud.add_points(self.temp_points)
        self.cat.move(self.speed)
        self.cat.update()
        for p in self.listPower:
            p.update()

