from constants import *
from src.factory.Hud import HudManager
from src.interfaces.SceneInteface import SceneInterface
from src.itemgame.LifeModel import LifeModel
from src.itemgame.SpecialModel import SpecialModel
from src.model.AirPlaneModel import AirPlaneModel
from src.model.BackgroundModel import BackgroundModel
from src.itemgame.CoinModel import CoinModel
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel


class BattleSceneFirst(SceneInterface):
    def __init__(self, hud: HudManager):
        self.hud = hud
        self.background = BackgroundModel(BACKGROUND_BATTLE1)
        self.air_plane = AirPlaneModel()
        self.enemy_plane = EnemyAirPlaneModel(700, 300)
        self.coin = CoinModel()
        self.life = LifeModel(WIDTH_SCREEN, HEIGHT_SCREEN / 2, True)
        self.special = SpecialModel(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, True)
        self.fps = 0

        self.game_objects = [self.background, self.enemy_plane, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(),
                             self.enemy_plane.get_shot()]

    def handle_event(self, fps, event, state):
        if not state:
            return

        self.fps = fps
        if event.key_pressed("UP"):  # Direcional ^
            self.air_plane.up(self.fps)
        if event.key_pressed("DOWN"):
            self.air_plane.down(self.fps)
        if event.key_pressed("RIGHT"):
            self.air_plane.forward(self.fps)
        if event.key_pressed("LEFT"):
            self.air_plane.backward(self.fps)
        if event.key_pressed("SPACE"):
            self.air_plane.shot()

        for game_object in self.game_objects:
            game_object.move(self.fps)

        if self.coin.collide(self.air_plane):
            self.coin.points += 1
            self.hud.add_points(self.coin.points)

        if self.life.collide(self.air_plane):
            self.life.disable_movimentation()
            self.hud.add_life()

        if self.special.collide(self.air_plane):
            self.special.disable_movimentation()
            self.hud.add_special()

        if self.air_plane.get_shot().collide(self.enemy_plane):
            if (self.enemy_plane.lifeModel.loseLife()) == 0:
                self.enemy_plane.hidden()

        if self.enemy_plane.get_shot().collide(self.air_plane):
            self.hud.lose_life()

        self.enemy_plane.can_shot(self.air_plane)

    def draw(self, state):
        # if state:

        for game_object in self.game_objects:
            game_object.draw()

        self.enemy_plane.get_life().draw()
        self.hud.draw()  # deve ser o ultimo

    def update(self, state):
        if not state:
            return

        for game_object in self.game_objects:
            game_object.update()
