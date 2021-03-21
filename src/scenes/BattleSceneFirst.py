from constants import *
from src.factory.Hud import HudManager
from src.interfaces.SceneInteface import SceneInterface
from src.itemgame.LifeModel import LifeModel
from src.itemgame.SpecialModel import SpecialModel
from src.model.AirPlaneModel import AirPlaneModel
from src.model.BackgroundModel import BackgroundModel
from src.itemgame.CoinModel import CoinModel


class BattleSceneFirst(SceneInterface):
    def __init__(self, hud: HudManager):
        self.hud = hud
        self.background = BackgroundModel(BACKGROUND_BATTLE1)
        self.airplane = AirPlaneModel()
        self.coin = CoinModel()
        self.life = LifeModel(WIDTH_SCREEN, HEIGHT_SCREEN / 2, True)
        self.special = SpecialModel(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, True)
        self.fps = 0

        self.game_objects = [self.background, self.airplane,
                             self.coin, self.life, self.special]

    def handle_event(self, fps, event, state):
        if not state:
            return

        self.fps = fps
        if event.key_pressed("UP"):  # Direcional ^
            self.airplane.up(self.fps)
        if event.key_pressed("DOWN"):
            self.airplane.down(self.fps)
        if event.key_pressed("RIGHT"):
            self.airplane.forward(self.fps)
        if event.key_pressed("LEFT"):
            self.airplane.backward(self.fps)

        for game_object in self.game_objects:
            game_object.move(self.fps)

        if self.coin.collide(self.airplane):
            self.coin.points += 1
            self.hud.add_points(self.coin.points)

        if self.life.collide(self.airplane):
            self.life.disable_movimentation()
            self.hud.add_life()

        if self.special.collide(self.airplane):
            self.special.disable_movimentation()
            self.hud.add_special()

    def draw(self, state):
        #if state:

        for game_object in self.game_objects:
            game_object.draw()

        self.hud.draw()  # deve ser o ultimo

    def update(self, state):
        if not state:
            return

        for game_object in self.game_objects:
            game_object.update()
