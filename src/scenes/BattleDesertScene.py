from constants import *

from src.factory.Hud import HudManager
from src.itemgame.ItemModel import ItemModel
from src.model.BackgroundModel import BackgroundModel
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel

from src.scenes.BattleSceneFirst import BattleSceneFirst


class BattleDesertScene(BattleSceneFirst):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.background = BackgroundModel(BACKGROUND_DESERT)

        self.wind = self.__wind_direction(RIGHT_ARROW)

        self.enemy_plane_two = EnemyAirPlaneModel(*ENEMY_PLANE_SECCOND_POSITION)

        self.game_objects = [self.background, self.enemy_plane, self.enemy_plane_two, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(), self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot(), self.enemy_plane_two.get_shot()]

        self.enemys = [self.enemy_plane, self.enemy_plane_two]
        self.enemy_shot_times = [0.0, 0.0]
        self.backward = False
        self.count = 0.0
        self.wind_force = 0.5

    def __wind_direction(self, image):
        windDirection = ItemModel(image)
        windDirectionAnimation = windDirection.animation
        windDirectionAnimation.set_position(WIDTH_SCREEN / 2,
                                            HEIGHT_SCREEN - windDirectionAnimation.width - 50)
        return windDirectionAnimation

    def handle_event(self, speed, state):
        super().handle_event(speed, state)
        self.count += speed / 150

        if self.count >= 1:
            self.count = 0
            self.wind_force += 0.1

        if self.wind_force >= 1.3:
            self.backward = not self.backward
            self.wind_force = 0.5
            if self.backward:
                self.wind = self.__wind_direction(LEFT_ARROW)
            else:
                self.wind = self.__wind_direction(RIGHT_ARROW)

        if self.backward:
            self.air_plane.backward(speed * self.wind_force)
        else:
            self.air_plane.forward(speed * self.wind_force)

    def update(self, state):
        if not state:
            return
        self.wind.draw()

        if self.point >= POINTS * 3:
            self.hud.get_window().main_scene.change_scene('Space')

        for game_object in self.game_objects:
            game_object.update()

        self.wind.update()
