from PPlay.gameimage import *

from src.interfaces.SceneInteface import SceneInterface

from src.itemgame.CoinModel import CoinModel

from src.model.CatModel import CatModel

from constants import *


class HomeScene(SceneInterface):

    def __init__(self, hud):
        self.hud = hud
        self.key_board = hud.get_window().get_keyboard()
        self.fundo = GameImage(BACKGROUND_HOME)
        self.cat = CatModel()
        self.speed = 0
        self.coin = CoinModel()
        self.listPower = self.coin.generatesPoint(GENERATED_POINTS)

    def handle_event(self, speed, state):
        if not state:
            return

        self.speed = speed
        if self.key_board.key_pressed("UP"):  # Direcional ^
            self.cat.jump()
        elif self.key_board.key_pressed("LEFT"):
            self.cat.walk_fliped()
        elif self.key_board.key_pressed("RIGHT"):
            self.cat.walk()
        else:
            self.cat.idle()

        for p in self.listPower:
            p.move(self.speed)
            if p.collide(self.cat):
                self.hud.add_points(1)

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

        self.cat.move(self.speed)
        self.cat.update()
        for p in self.listPower:
            p.update()

