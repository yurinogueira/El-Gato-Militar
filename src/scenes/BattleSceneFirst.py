from PPlay.gameimage import GameImage
from constants import *
from src.factory.Hud import HudManager
from src.factory.Text import CenterText
from src.interfaces.SceneInteface import SceneInterface
from src.itemgame.CoinModel import CoinModel
from src.itemgame.LifeModel import LifeModel
from src.itemgame.SpecialModel import SpecialModel
from src.model.AirPlaneModel import AirPlaneModel
from src.model.BackgroundModel import BackgroundModel
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel


class BattleSceneFirst(SceneInterface):
    def __init__(self, hud: HudManager):
        self.hud = hud
        self.window = hud.get_window()
        self.key_board = hud.get_window().get_keyboard()
        self.background = BackgroundModel(BACKGROUND_BATTLE1)
        self.air_plane = AirPlaneModel(shoot=self.hud.get_special_look(), sprite=self.hud.get_ship_look())
        self.enemy_plane = EnemyAirPlaneModel(*ENEMY_PLANE_FIRST_POSITION)
        self.coin = CoinModel()
        self.life = LifeModel(WIDTH_SCREEN, HEIGHT_SCREEN / 2, True)
        self.special = SpecialModel(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, True)
        self.point = 0
        points_background = pygame.transform.scale(GameImage(SOUND_BACKGROUND).image, (250, 90))
        self.point_background = GameImage(SOUND_BACKGROUND)
        self.point_background.image = points_background
        self.point_background.set_position(self.window.width / 2 - points_background.get_width() / 2, -15)
        self.shot_time = 0.0

        self.game_objects = [self.background, self.enemy_plane, self.air_plane,
                             self.coin, self.life, self.special,
                             self.air_plane.get_shot(),
                             self.air_plane.get_shot_special(),
                             self.enemy_plane.get_shot()]
        self.enemys = [self.enemy_plane]
        self.enemy_shot_times = [0.0]

    def handle_event(self, speed, state):
        if not state:
            return

        self.shot_time -= self.hud.get_window().delta_time()

        for i in range(len(self.enemys)):
            self.enemy_shot_times[i] -= self.hud.get_window().delta_time()

            if self.air_plane.get_shot().collide(self.enemys[i]):
                self.point += 1

                if self.point % 4 == 0:
                    self.special.change_visibility(self.enemys[i].animation.x, self.enemys[i].animation.y)
                if self.point % 5 == 0:
                    self.life.change_visibility(self.enemys[i].animation.x, self.enemys[i].animation.y)

                if (self.enemys[i].lifeModel.lose_life()) == 0:
                    self.enemys[i].hidden()

            if self.air_plane.get_shot_special().collide(self.enemys[i]):
                self.point += 3
                self.enemys[i].lifeModel.empty_life()
                self.enemys[i].hidden()

            if self.enemys[i].get_shot().collide(self.air_plane):
                self.hud.lose_life()

            if self.enemy_shot_times[i] <= 0.0:
                self.enemys[i].can_shot(self.air_plane)
                self.enemy_shot_times[i] = 2

        if self.key_board.key_pressed("UP"):  # Direcional ^
            self.air_plane.up(speed * 2)
        if self.key_board.key_pressed("DOWN"):
            self.air_plane.down(speed * 2)
        if self.key_board.key_pressed("RIGHT"):
            self.air_plane.forward(speed * 2)
        if self.key_board.key_pressed("LEFT"):
            self.air_plane.backward(speed * 2)
        if self.shot_time <= 0.0:
            if self.key_board.key_pressed("SPACE"):
                self.air_plane.shot()
                self.shot_time = 1
        if self.key_board.key_pressed("S") and self.hud.get_special() >= 4:
            self.hud.lose_special()
            self.air_plane.shot_special()

        for game_object in self.game_objects:
            game_object.move(speed)

        if self.coin.collide(self.air_plane):
            self.hud.point.addPoint(1)

        if self.life.collide(self.air_plane):
            self.life.change_visibility()
            self.hud.add_life()

        if self.special.collide(self.air_plane):
            self.special.change_visibility()
            self.hud.add_special()

    def draw(self, state):

        for game_object in self.game_objects:
            game_object.draw()

        for enemy in self.enemys:
            enemy.get_life().draw()

        self.hud.draw()
        self.point_background.draw()


        CenterText(self.hud.get_window(),
                   self.hud.get_window().width / 2,
                   30, GOLD, 64, "Pontos " + str(self.point)).draw()

    def update(self, state):
        if not state:
            return

        if self.point >= POINTS:
            self.hud.get_window().main_scene.change_scene('SecondHistory')

        for game_object in self.game_objects:
            game_object.update()
