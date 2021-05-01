from constants import *
from src.factory.Hud import HudManager
from src.factory.Text import CenterText
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
        self.key_board = hud.get_window().get_keyboard()
        self.background = BackgroundModel(BACKGROUND_BATTLE1)
        self.air_plane = AirPlaneModel(shoot=self.hud.get_special_look(), sprite=self.hud.get_ship_look())
        self.enemy_plane = EnemyAirPlaneModel(*ENEMY_PLANE_FIRST_POSITION)
        self.coin = CoinModel()
        self.life = LifeModel(WIDTH_SCREEN, HEIGHT_SCREEN / 2, True)
        self.special = SpecialModel(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, True)
        self.fps = 0
        self.point = 0

        self.game_objects = [self.background, self.enemy_plane, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(),
                             self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot()]
        self.shot_enemy_time = 0.0
        self.shot_time = 0.0

    def handle_event(self, fps, state):
        if not state:
            return

        if self.point >= POINTS:
            import main
            main.change_scene('Select')

        self.shot_enemy_time -= self.hud.get_window().delta_time()
        self.shot_time -= self.hud.get_window().delta_time()
        self.fps = fps

        if self.key_board.key_pressed("UP"):  # Direcional ^
            self.air_plane.up(self.fps)
        if self.key_board.key_pressed("DOWN"):
            self.air_plane.down(self.fps)
        if self.key_board.key_pressed("RIGHT"):
            self.air_plane.forward(self.fps)
        if self.key_board.key_pressed("LEFT"):
            self.air_plane.backward(self.fps)
        if self.shot_time <= 0.0:
            if self.key_board.key_pressed("SPACE"):
                self.air_plane.shot()
                self.shot_time = 1
        if self.key_board.key_pressed("S") and self.hud.get_special() >= 4:
            self.hud.lose_special()
            self.air_plane.shot_special()

        for game_object in self.game_objects:
            game_object.move(self.fps)

        if self.coin.collide(self.air_plane):
            self.hud.point.addPoint(1)

        if self.life.collide(self.air_plane):
            self.life.change_visibility()
            self.hud.add_life()

        if self.special.collide(self.air_plane):
            self.special.change_visibility()
            self.hud.add_special()

        if self.air_plane.get_shot().collide(self.enemy_plane):
            self.point += 1

            if self.point % 4 == 0:
                self.special.change_visibility(self.enemy_plane.animation.x, self.enemy_plane.animation.y)
            if self.point % 5 == 0:
                self.life.change_visibility(self.enemy_plane.animation.x, self.enemy_plane.animation.y)

            if (self.enemy_plane.lifeModel.lose_life()) == 0:
                self.enemy_plane.hidden()

        if self.air_plane.get_shot_special().collide(self.enemy_plane):
            self.point += 3
            self.enemy_plane.lifeModel.empty_life()
            self.enemy_plane.hidden()

        if self.enemy_plane.get_shot().collide(self.air_plane):
            self.hud.lose_life()

        if self.shot_enemy_time <= 0.0:
            self.enemy_plane.can_shot(self.air_plane)
            self.shot_enemy_time = 2

    def draw(self, state):

        for game_object in self.game_objects:
            game_object.draw()

        self.enemy_plane.get_life().draw()
        self.hud.draw()

        choose_color = NEAR_BLACK

        if 10 > self.point > 5:
            choose_color = GOLD
        elif 15 > self.point > 9:
            choose_color = ORANGE
        elif self.point > 15:
            choose_color = GOLDEN

        CenterText(self.hud.get_window(),
                   self.hud.get_window().width / 2,
                   30, choose_color, 64, "Pontos " + str(self.point)).draw()

    def update(self, state):
        if not state:
            return

        for game_object in self.game_objects:
            game_object.update()
