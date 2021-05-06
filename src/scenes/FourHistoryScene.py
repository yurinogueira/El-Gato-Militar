from PPlay.gameimage import GameImage

from src.factory.Button import Button
from src.factory.Hud import HudManager
from src.factory.Text import CenterText
from src.scenes.FirstHistoryScene import FirstHistoryScene

from constants import *


class FourHistoryScene(FirstHistoryScene):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.hud = hud
        self.window = hud.get_window()
        self.fundo = GameImage(BACKGROUND_HISTORY)

        self.text_one = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 130, color=BLACK, size=56,
                                   text="Eles chegaram ao espaço...")
        self.text_two = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 100, color=BLACK, size=36,
                                   text="Agora os cachorros militares possuem a arma de")
        self.text_three = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 70, color=BLACK, size=36,
                                     text="destruição em massa, você precisa derrota-los antes")
        self.four = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 40, color=BLACK, size=36,
                               text="que eles consigam destruir todo o planeta")
        self.five = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 10, color=BLACK, size=36,
                               text="você precisa derrotar todos eles, caso algum volte")
        self.six = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV + 20, color=BLACK, size=36,
                              text="ele poderá se preparar para um retorno!")
        self.points_text = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV + 70, color=SKY_BLUE, size=56,
                                      text="Objetivo: Junte 20 Pontos")

        self.button_continuar = Button(self.window, WINDOW_SIZE[0] - 200, WINDOW_SIZE[1] - 100, "CERTO!")

    def update(self, state: bool):
        if self.button_continuar.is_button_pressed():
            self.window.main_scene.change_scene('Space')
