from constants import *


class SoundControl:
    def __init__(self):
        self.old_scene = 'MenuScene'
        self.is_enabled = True

        self.menu_music = MENU_LOOP_SOUND
        self.battle_music = SIMPLE_BATTLE_SOUND
        self.double_music = DOUBLE_BATTLE_SOUND
        self.mega_battle_music = MEGA_BATTLE_MUSIC

        self.menu_music.set_repeat(True)
        self.battle_music.set_repeat(True)
        self.double_music.set_repeat(True)
        self.mega_battle_music.set_repeat(True)

    def get_sound_state(self) -> bool:
        return self.is_enabled

    def change_sound_state(self):
        self.is_enabled = not self.is_enabled

    def play_music(self, class_name: str):
        if not self.get_sound_state():
            self.menu_music.pause()
        else:
            self.menu_music.unpause()
            if self.old_scene != class_name:
                self.old_scene = class_name
                self.menu_music.stop()
                self.battle_music.stop()
                self.double_music.stop()
                self.mega_battle_music.stop()

            if not self.menu_music.is_playing() and class_name == 'MenuScene':
                self.menu_music.play()
            if not self.battle_music.is_playing() and class_name == 'BattleSceneFirst':
                self.battle_music.play()
            if not self.menu_music.is_playing() and class_name == 'SelectPlaneScene':
                self.menu_music.play()
            if not self.menu_music.is_playing() and class_name == 'HomeScene':
                self.menu_music.play()
            if not self.battle_music.is_playing() and class_name == 'BattleSceneSeccond':
                self.battle_music.play()
            if not self.double_music.is_playing() and class_name == 'BattleSceneFinal':
                self.double_music.play()
            if not self.mega_battle_music.is_playing() and class_name == 'BattleSpaceScene':
                self.mega_battle_music.play()
