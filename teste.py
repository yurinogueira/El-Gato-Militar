from PPlay.window import *

# Janela e HUD
from constants import WINDOW_SIZE
from src.factory.Hud import HudManager
from src.scenes.HomeScene import HomeScene
from src.scenes.BattleSceneFirst import BattleSceneFirst

window = Window(*WINDOW_SIZE)
hud = HudManager(window)

key_board = window.get_keyboard()

scenes = {
    'Main': HomeScene(hud),
    'Battle': BattleSceneFirst(hud)
}

scene = scenes['Main']


def change_scene(scene_key):
    global scene
    scene = scenes[scene_key]


# Loop
while True:
    SPEED_PER_FRAME = 120 * window.delta_time()

    scene.handle_event(SPEED_PER_FRAME, key_board)
    scene.draw()
    scene.update()

    window.update()
