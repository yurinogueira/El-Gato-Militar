from PPlay.window import *
import constants as CONST
from src.model.CatModel import CatModel


janela = Window(*CONST.WINDOW_SIZE)

key_board = Window.get_keyboard()

cat = CatModel()

# Loop
while True:
    SPEED_PER_FRAME = 60 * janela.delta_time()

    janela.set_background_color((27, 215, 100))

    if key_board.key_pressed("UP"):  # Direcional ^
        cat.jump()
    elif key_board.key_pressed("DOWN"):  # Direcional \/
        print("Baixo!")
    elif key_board.key_pressed("LEFT"):  # Direcional
        print("Direita!")
    elif not cat.is_playing():
        cat.walk()

    # ANIMATION
    cat.move(SPEED_PER_FRAME)

    # DRAW
    cat.draw()

    # UPDATE
    cat.update()
    janela.update()

