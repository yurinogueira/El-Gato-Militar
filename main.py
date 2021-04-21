from PPlay.window import *

# Janela e HUD
from constants import WINDOW_SIZE
from src.scenes.MenuScene import MenuScene
from src.scenes.HomeScene import HomeScene
from src.scenes.BattleSceneFirst import BattleSceneFirst


running = True
window = Window(*WINDOW_SIZE)
scene = MenuScene(window)


def change_scene(scene_key='Main'):
    global scene
    scenes = {
        'Home': HomeScene(scene.hud),
        'Main': MenuScene(window),
        'Battle': BattleSceneFirst(scene.hud)
    }
    scene = scenes[scene_key]


# Loop
while True:
    SPEED_PER_FRAME = 200 * window.delta_time()

    scene.handle_event(SPEED_PER_FRAME, window.get_keyboard(), running)
    scene.draw(running)
    scene.update(running)

    window.update()
