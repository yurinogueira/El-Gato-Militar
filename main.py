from PPlay.window import *

from src.factory.SoundControl import SoundControl

from src.scenes.MenuScene import MenuScene
from src.scenes.HomeScene import HomeScene
from src.scenes.SelectPlaneScene import SelectPlaneScene
from src.scenes.BattleSceneFirst import BattleSceneFirst
from src.scenes.BattleSceneSeccond import BattleSceneSeccond
from src.scenes.BattleSceneFinal import BattleSceneFinal
from src.scenes.BattleDesertScene import BattleDesertScene
from src.scenes.BattleSpaceScene import BattleSpaceScene
from src.scenes.BattleCityScene import BattleCityScene
from src.scenes.GameOverScene import GameOverScene

from constants import WINDOW_SIZE, SPEED, TITLE


class Main:
    def __init__(self):
        self.running = True

        self.window = Window(*WINDOW_SIZE)
        self.window.set_title(TITLE)
        self.window.sound = SoundControl()
        self.window.main_scene = self

        self.scene = MenuScene(self.window)

    def get_hud(self):
        return self.scene.hud

    def change_scene(self, scene_key='Main'):
        self.scene = {
            'Main': MenuScene(self.window),
            'Battle': BattleSceneSeccond(self.get_hud()),
            'BattleFirst': BattleSceneFirst(self.get_hud()),
            'Select': SelectPlaneScene(self.get_hud()),
            'Home': HomeScene(self.get_hud()),
            'Boss': BattleSceneFinal(self.get_hud()),
            'Desert': BattleDesertScene(self.get_hud()),
            'Space': BattleSpaceScene(self.get_hud()),
            'City': BattleCityScene(self.get_hud()),
            'Over': GameOverScene(self.get_hud())
        }[scene_key]

    def start(self):
        while True:
            delta_time = self.window.delta_time()
            if delta_time == 0:
                delta_time = 1

            speed = SPEED * delta_time

            self.scene.handle_event(speed, self.running)
            self.scene.draw(self.running)
            self.scene.update(self.running)

            self.window.sound.play_music(self.scene.__class__.__name__)
            self.window.update()


main_class = Main()
main_class.start()
