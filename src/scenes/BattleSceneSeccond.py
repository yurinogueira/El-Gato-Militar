from constants import *

from src.factory.Hud import HudManager
from src.model.AllyPlaneModel import AllyPlaneModel

from src.scenes.BattleSceneFirst import BattleSceneFirst


class BattleSceneSeccond(BattleSceneFirst):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.pipoca_plane = AllyPlaneModel(*ENEMY_PLANE_SECCOND_POSITION)

        self.game_objects = [self.background, self.enemy_plane, self.pipoca_plane, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(), self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot()]

    def update(self, state):
        if not state:
            return

        if self.point >= POINTS * 2:
            import main
            main.change_scene('Boss')

        for game_object in self.game_objects:
            game_object.update()
