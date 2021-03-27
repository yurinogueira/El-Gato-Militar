from PPlay.window import *

# Janela e HUD
from constants import WINDOW_SIZE
from src.factory.Hud import HudManager
from src.scenes.MenuScene import MenuScene
from src.scenes.HomeScene import HomeScene
from src.scenes.BattleSceneFirst import BattleSceneFirst


running = True
window = Window(*WINDOW_SIZE)
hud = HudManager(window)

scenes = {
    'Home': HomeScene(hud),
    'Main': MenuScene(hud),
    'Battle': BattleSceneFirst(hud)
}

scene = scenes['Main']


def change_scene(scene_key='Main'):
    global scene
    scene = scenes[scene_key]


def change_state(state=True):
    global running
    running = state


def get_state():
    global running
    return running


# Loop
while True:
    SPEED_PER_FRAME = 200 * window.delta_time()

    scene.handle_event(SPEED_PER_FRAME, window.get_keyboard(), running)
    scene.draw(running)
    scene.update(running)

    window.update()
