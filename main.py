from PPlay.window import *

from src.scenes.MenuScene import MenuScene
from src.scenes.HomeScene import HomeScene
from src.scenes.SelectPlaneScene import SelectPlaneScene
from src.scenes.BattleSceneFirst import BattleSceneFirst
from src.scenes.BattleSceneSeccond import BattleSceneSeccond
from src.scenes.BattleSceneFinal import BattleSceneFinal
from src.scenes.BattleDesertScene import BattleDesertScene
from src.scenes.BattleSpaceScene import BattleSpaceScene
from src.scenes.BattleCityScene import BattleCityScene

from src.factory.SoundControl import SoundControl

from constants import WINDOW_SIZE, FRAME_SPEED, TITLE


running = True

window = Window(*WINDOW_SIZE)
window.set_title(TITLE)
window.sound = SoundControl()

scene = MenuScene(window)


def get_hud():
    return scene.hud


def change_scene(scene_key='Main'):
    global scene
    scene = {
        'Main': MenuScene(window),
        'Battle': BattleSceneSeccond(scene.hud),
        'BattleFirst': BattleSceneFirst(scene.hud),
        'Select': SelectPlaneScene(scene.hud),
        'Home': HomeScene(scene.hud),
        'Boss': BattleSceneFinal(scene.hud),
        'Desert': BattleDesertScene(scene.hud),
        'Space': BattleSpaceScene(scene.hud),
        'City': BattleCityScene(scene.hud)
    }[scene_key]


# Loop
while True:
    SPEED_PER_FRAME = FRAME_SPEED * window.delta_time()

    scene.handle_event(SPEED_PER_FRAME, running)
    scene.draw(running)
    scene.update(running)

    window.sound.play_music(scene.__class__.__name__)

    window.update()
