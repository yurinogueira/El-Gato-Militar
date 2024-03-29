from constants import *

from src.scenes.BattleSceneFirst import BattleSceneFirst

from src.factory.Hud import HudManager

from src.itemgame.BlackHoleModel import BlackHoleModel

from src.model.BackgroundModel import BackgroundModel
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel


class BattleSpaceScene(BattleSceneFirst):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.background = BackgroundModel(BACKGROUND_SPACE)
        self.enemy_plane_two = EnemyAirPlaneModel(*ENEMY_PLANE_SECCOND_POSITION)
        self.blackHole = BlackHoleModel(WIDTH_SCREEN / 2, 0)
        self.game_objects = [self.background, self.enemy_plane, self.enemy_plane_two, self.air_plane,
                             self.coin, self.life, self.special, self.blackHole,
                             self.air_plane.get_shot(), self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot(), self.enemy_plane_two.get_shot()]

        self.enemys = [self.enemy_plane, self.enemy_plane_two]
        self.enemy_shot_times = [0.0, 0.0]
        self.backward = True
        self.count = 0
        self.wind = 0.5

    def handle_event(self, speed, state):
        super().handle_event(speed, state)
        self.blackHole.attraction(speed, self.air_plane)
        if self.blackHole.collide(self.air_plane):
            self.hud.game_over()
        self.blackHole.draw()

    def update(self, state):
        if not state:
            return

        if self.point >= POINTS:
            self.hud.get_window().main_scene.change_scene('FiveHistoryScene')

        for game_object in self.game_objects:
            game_object.update()
        self.blackHole.update()
