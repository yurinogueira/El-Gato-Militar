from constants import *

from src.factory.Hud import HudManager
from src.model.BackgroundModel import BackgroundModel
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel

from src.scenes.BattleSceneFirst import BattleSceneFirst


class BattleDesertScene(BattleSceneFirst):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.background = BackgroundModel(BACKGROUND_DESERT)
        self.enemy_plane_two = EnemyAirPlaneModel(*ENEMY_PLANE_SECCOND_POSITION)

        self.game_objects = [self.background, self.enemy_plane, self.enemy_plane_two, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(), self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot(), self.enemy_plane_two.get_shot()]

        self.enemys = [self.enemy_plane, self.enemy_plane_two]
        self.enemy_shot_times = [0.0, 0.0]
        self.backward = False
        self.count = 0
        self.wind = 0.5

    def handle_event(self, fps, state):
        super().handle_event(fps, state)
        self.count += 1

        if self.count % 60 == 0:
            self.count = 0
            self.wind += 0.1

        if self.backward:
            self.background.move(-fps*2)
            if self.wind >= 1.3:
                self.wind = 0.5
                self.backward = False

            self.air_plane.backward(self.fps * self.wind)
        else:
            self.background.move(fps*1)
            if self.wind >= 1.3:
                self.wind = 0.5
                self.backward = True

            self.air_plane.forward(self.fps * self.wind)

    def update(self, state):
        if not state:
            return

        if self.point >= POINTS * 3:
            self.hud.get_window().main_scene.change_scene('Space')

        for game_object in self.game_objects:
            game_object.update()
