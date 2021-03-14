from PPlay.window import *
from PPlay.gameimage import *
import constants as CONST


# Janela e HUD
from src.scenes.HomeScene import HomeScene
from src.scenes.BattleSceneFirst import BattleSceneFirst


janela = Window(*CONST.WINDOW_SIZE)
scenes = {'Main': HomeScene(),
          'Battle': BattleSceneFirst()}

scene = scenes['Main']

bar_points = GameImage(CONST.POINTS_HUD)
bar_points.set_position(janela.width - bar_points.width, 0)

bar_time = GameImage(CONST.TIME_HUD)
bar_time.set_position(janela.width / 2 - bar_time.width / 2, 0)

# Vars
points = 0
tempo = 60

key_board = Window.get_keyboard()


def points_hud(amount):
    bar_points.draw()
    font = pygame.font.Font(None, 64)
    text = font.render(str(amount), True, CONST.WHITE)
    text_rect = text.get_rect(center=(janela.width - bar_points.width / 2 - 16, 64))
    janela.screen.blit(text, text_rect)


def time_hud():
    bar_time.draw()
    seconds = (janela.time_elapsed() / 1000) % 60
    seconds = tempo - seconds
    if seconds == 0:
        scene = scenes['Battle']
    font = pygame.font.Font(None, 64)
    text = font.render(str(int(seconds)), True, CONST.WHITE)
    text_rect = text.get_rect(center=(janela.width / 2, 58))
    janela.screen.blit(text, text_rect)


# Loop
while True:

    #fundo.draw()

    SPEED_PER_FRAME = 120 * janela.delta_time()


    scene.handle_event(SPEED_PER_FRAME, key_board)
    scene.draw()
    scene.update()

    # TEM QUE REMOVER
    points = scene.points

    # HUD
    points_hud(points)
    time_hud()

    janela.update()



