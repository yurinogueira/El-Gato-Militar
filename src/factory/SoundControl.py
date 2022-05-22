from constants import *


class SoundControl:
    def __init__(self):
        self.old_scene = ''
        self.is_enabled = True

        self.menu_music = MENU_LOOP_SOUND
        self.menu_music.set_volume(5)
        self.battle_music = SIMPLE_BATTLE_SOUND
        self.battle_music.set_volume(5)
        self.double_music = DOUBLE_BATTLE_SOUND
        self.double_music.set_volume(5)
        self.mega_battle_music = MEGA_BATTLE_MUSIC
        self.mega_battle_music.set_volume(5)

        self.menu_music.set_repeat(True)
        self.battle_music.set_repeat(True)
        self.double_music.set_repeat(True)
        self.mega_battle_music.set_repeat(True)

    def get_sound_state(self) -> bool:
        return self.is_enabled

    def change_sound_state(self):
        self.is_enabled = not self.is_enabled
        if not self.get_sound_state():
            self.menu_music.stop()
            self.battle_music.stop()
            self.double_music.stop()
            self.mega_battle_music.stop()

    def play_music(self, class_name: str):
        if not self.get_sound_state():
            return

        if self.old_scene != class_name:
            self.old_scene = class_name
            self.menu_music.stop()
            self.battle_music.stop()
            self.double_music.stop()
            self.mega_battle_music.stop()

        if class_name == 'MenuScene':
            self.menu_music.play()
        if class_name == 'BattleSceneFirst':
            self.battle_music.play()
        if class_name == 'HomeScene':
            self.menu_music.play()
        if class_name == 'BattleCityScene':
            self.menu_music.play()
        if class_name == 'BattleDesertScene':
            self.battle_music.play()
        if class_name == 'BattleSceneFinal':
            self.double_music.play()
        if class_name == 'BattleSpaceScene':
            self.mega_battle_music.play()
