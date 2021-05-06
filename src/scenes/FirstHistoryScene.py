from PPlay.gameimage import GameImage

from src.factory.Button import Button
from src.factory.Hud import HudManager
from src.factory.Text import CenterText
from src.interfaces.SceneInteface import SceneInterface

from constants import *


class FirstHistoryScene(SceneInterface):
    def __init__(self, hud: HudManager):
        self.hud = hud
        self.window = hud.get_window()
        self.fundo = GameImage(BACKGROUND_HISTORY)

        self.text_one = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 130, color=BLACK, size=56,
                                   text="Olá novamente Gato Militar!")
        self.text_two = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 100, color=BLACK, size=36,
                                   text="O mundo precisa novamente de seus serviços")
        self.text_three = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 70, color=BLACK, size=36,
                                     text="Os cachorros militares estão tentando roubar")
        self.four = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 40, color=BLACK, size=36,
                               text="uma arma de destruição em massa, não podemos")
        self.five = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV - 10, color=BLACK, size=36,
                               text="permitir isso, aproveite que ainda estão nas")
        self.six = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV + 20, color=BLACK, size=36,
                              text="colinas! Impeça-os!")
        self.points_text = CenterText(self.window, WIDTH_DIV, HEIGHT_DIV + 70, color=SKY_BLUE, size=56,
                                      text="Objetivo: Junte 20 pontos")

        self.button_continuar = Button(self.window, WINDOW_SIZE[0] - 200, WINDOW_SIZE[1] - 100, "CERTO!")

    def handle_event(self, speed: int, scene: bool):
        pass

    def draw(self, state: bool):
        self.fundo.draw()
        self.text_one.draw()
        self.text_two.draw()
        self.text_three.draw()
        self.four.draw()
        self.five.draw()
        self.six.draw()
        self.points_text.draw()
        self.button_continuar.draw()

    def update(self, state: bool):
        if self.button_continuar.is_button_pressed():
            self.window.main_scene.change_scene('BattleFirst')
