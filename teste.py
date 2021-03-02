from PPlay.window import *
from PPlay.gameimage import *
from src.model.CatModel import CatModel
from src.model.PowerUpModel import PowerUpModel
import constants as CONST

# Janela e HUD
janela = Window(*CONST.WINDOW_SIZE)

bar_points = GameImage(CONST.POINTS_HUD)
bar_points.set_position(janela.width - bar_points.width, 0)

bar_time = GameImage(CONST.TIME_HUD)
bar_time.set_position(janela.width / 2 - bar_time.width / 2, 0)

# Vars
points = 0

key_board = Window.get_keyboard()

cat = CatModel()

powers = []

for i in range(CONST.POINTS):
    powers.append(PowerUpModel())


def points_hud(amount):
    bar_points.draw()
    font = pygame.font.Font(None, 64)
    text = font.render(str(amount), True, CONST.WHITE)
    text_rect = text.get_rect(center=(janela.width - bar_points.width / 2 - 16, 64))
    janela.screen.blit(text, text_rect)


def time_hud():
    bar_time.draw()
    seconds = (janela.time_elapsed() / 1000) % 60
    font = pygame.font.Font(None, 64)
    text = font.render(str(int(seconds)), True, CONST.WHITE)
    text_rect = text.get_rect(center=(janela.width / 2, 58))
    janela.screen.blit(text, text_rect)


def spawn_points():
    temp_points = 0

    for p in powers:
        p.move()
        p.draw()
        temp_points += p.collide(cat)
        p.update()

    return temp_points


# Loop
while True:
    SPEED_PER_FRAME = 120 * janela.delta_time()

    janela.set_background_color((27, 215, 100))

    if key_board.key_pressed("UP"):  # Direcional ^
        cat.jump(300)
    # elif key_board.key_pressed("DOWN"):  # Direcional \/
    #     print("Baixo!")
    # elif key_board.key_pressed("LEFT"):  # Direcional
    #     print("Direita!")
    elif not cat.is_playing():
        cat.walk()

    cat.move(SPEED_PER_FRAME)

    # POINTS
    points += spawn_points()

    # DRAW
    cat.draw()

    # HUD
    points_hud(points)
    time_hud()

    # UPDATE
    cat.update()

    janela.update()
