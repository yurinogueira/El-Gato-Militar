from PPlay.gameimage import GameImage

from src.factory.Button import Button
from src.factory.Hud import HudManager
from src.factory.Text import CenterText
from src.scenes.FirstHistoryScene import FirstHistoryScene

from constants import *


class FiveHistoryScene(FirstHistoryScene):
    def __init__(self, hud: HudManager):
        super().__init__(hud)
        self.hud = hud
        self.window = hud.get_window()
        self.fundo = GameImage(BACKGROUND_HISTORY)

        self.text_one = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 130, color=BLACK, size=56,
                                   text="Você conseguiu Gato Militar!")
        self.text_two = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 100, color=BLACK, size=36,
                                   text="Você derrotou as forças dos cachorros")
        self.text_three = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 70, color=BLACK, size=36,
                                     text="militares! Mas ainda existem alguns na terra")
        self.four = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 40, color=BLACK, size=36,
                               text="volte até lá e derrote-os, depois disso você")
        self.five = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 10, color=BLACK, size=36,
                               text="estará liberado para ir para casa beber")
        self.six = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV + 20, color=BLACK, size=36,
                              text="leite com biscoitos!")
        self.points_text = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV + 70, color=SKY_BLUE, size=56,
                                      text="Objetivo: Junte 40 Pontos")

        self.button_continuar = Button(self.window, WINDOW_SIZE[0] - 200, WINDOW_SIZE[1] - 100, "CERTO!")

    def update(self, state: bool):
        if self.button_continuar.is_button_pressed():
            self.window.main_scene.change_scene('Boss')
