from PPlay.sprite import Sprite
from constants import *

from src.factory.Hud import HudManager
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel

from src.scenes.BattleSceneFirst import BattleSceneFirst


class BattleSceneFinal(BattleSceneFirst):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.background = Sprite(BACKGROUND_WAR)
        self.background.set_total_duration(1000)
        self.background.set_position(0, 0)

        self.enemy_plane_two = EnemyAirPlaneModel(*ENEMY_PLANE_SECCOND_POSITION)
        self.enemy_plane_three = EnemyAirPlaneModel(*ENEMY_PLANE_THREE_POSITION)
        self.enemy_plane_four = EnemyAirPlaneModel(*ENEMY_PLANE_FOUR_POSITION)

        self.game_objects = [self.enemy_plane, self.enemy_plane_two, self.enemy_plane_three, self.enemy_plane_four,
                             self.air_plane, self.coin, self.life, self.special,
                             self.air_plane.get_shot(), self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot(), self.enemy_plane_two.get_shot(),
                             self.enemy_plane_three.get_shot(), self.enemy_plane_four.get_shot()]

        self.enemys = [self.enemy_plane, self.enemy_plane_two, self.enemy_plane_three, self.enemy_plane_four]
        self.enemy_shot_times = [0.0, 0.0, 0.0, 0.0]

    def handle_event(self, speed, state):
        super().handle_event(speed, state)
        self.background.draw()

    def update(self, state):
        if not state:
            return
        self.background.update()
        if self.point >= POINTS * 2:
            self.hud.get_window().main_scene.change_scene('EndGame')

        for game_object in self.game_objects:
            game_object.update()
