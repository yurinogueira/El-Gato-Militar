import os
import sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###

from pplay.window import Window

from src.factory.SoundControl import SoundControl

from src.scenes.HistoryScene import HistoryScene
from src.scenes.MenuScene import MenuScene
from src.scenes.BattleSceneFirst import BattleSceneFirst
from src.scenes.SelectPlaneScene import SelectPlaneScene
from src.scenes.BattleDesertScene import BattleDesertScene
from src.scenes.HomeScene import HomeScene
from src.scenes.BattleCityScene import BattleCityScene
from src.scenes.BattleSpaceScene import BattleSpaceScene
from src.scenes.BattleSceneFinal import BattleSceneFinal
from src.scenes.GameOverScene import GameOverScene

from constants import WINDOW_SIZE, SPEED, TITLE, HISTORY_1, HISTORY_2, HISTORY_3, HISTORY_4, HISTORY_5, HISTORY_6, \
    BACKGROUND_HOME_END


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
            'FirstHistory': HistoryScene(self.get_hud(), HISTORY_1, "BattleFirst"),
            'BattleFirst': BattleSceneFirst(self.get_hud()),
            'SecondHistory': HistoryScene(self.get_hud(), HISTORY_2, "Select"),
            'Select': SelectPlaneScene(self.get_hud()),
            'Desert': BattleDesertScene(self.get_hud()),
            'ThirdHistoryScene': HistoryScene(self.get_hud(), HISTORY_3, "Home"),
            'Home': HomeScene(self.get_hud()),
            'City': BattleCityScene(self.get_hud()),
            'FourHistoryScene': HistoryScene(self.get_hud(), HISTORY_4, "Space"),
            'Space': BattleSpaceScene(self.get_hud()),
            'FiveHistoryScene': HistoryScene(self.get_hud(), HISTORY_5, "Boss"),
            'Boss': BattleSceneFinal(self.get_hud()),
            'Over': GameOverScene(self.get_hud()),
            'EndGame':  HistoryScene(self.get_hud(), HISTORY_6, "End"),
            'End':  HistoryScene(self.get_hud(), BACKGROUND_HOME_END, "End", False)

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
