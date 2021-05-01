from constants import *

from src.factory.Hud import HudManager
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel

from src.scenes.BattleSceneFirst import BattleSceneFirst


class BattleSceneFinal(BattleSceneFirst):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.enemy_plane_two = EnemyAirPlaneModel(*ENEMY_PLANE_SECCOND_POSITION)

        self.game_objects = [self.background, self.enemy_plane, self.enemy_plane_two, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(), self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot(), self.enemy_plane_two.get_shot()]

        self.enemys = [self.enemy_plane, self.enemy_plane_two]
        self.enemy_shot_times = [0.0, 0.0]

    def update(self, state):
        if not state:
            return

        if self.point >= POINTS * 3:
            import main
            main.change_scene('Main')

        for game_object in self.game_objects:
            game_object.update()
