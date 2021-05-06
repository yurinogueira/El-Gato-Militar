from constants import *

from src.factory.Hud import HudManager
from src.itemgame.CarModel import CarModel
from src.model.BackgroundModel import BackgroundModel
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel

from src.scenes.BattleSceneFirst import BattleSceneFirst


class BattleCityScene(BattleSceneFirst):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.background = BackgroundModel(BACKGROUND_CITY)
        self.enemy_plane_two = EnemyAirPlaneModel(*ENEMY_PLANE_SECCOND_POSITION)
        self.game_objects = [self.background, CarModel(109, CAR_1, True), CarModel(751, CAR_3, True),
                             CarModel(109, CAR_2), CarModel(997, CAR_4, True), CarModel(479, CAR_5),
                             self.enemy_plane, self.enemy_plane_two, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(), self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot(), self.enemy_plane_two.get_shot()]

        self.enemys = [self.enemy_plane, self.enemy_plane_two]
        self.enemy_shot_times = [0.0, 0.0]

    def update(self, state):
        if not state:
            return

        if self.point >= POINTS // 2:
            self.hud.get_window().main_scene.change_scene('FourHistoryScene')

        for game_object in self.game_objects:
            game_object.update()
