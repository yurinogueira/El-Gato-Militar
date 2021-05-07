from PPlay.gameimage import *

from src.interfaces.SceneInteface import SceneInterface

from src.factory.Button import Button, ButtonClick
from src.factory.Hud import HudManager
from src.factory.Text import CenterText

from constants import *


class MenuScene(SceneInterface):
    def __init__(self, window):
        self.hud = HudManager(window)
        self.window = window
        self.fundo = GameImage(BACKGROUND_HOME_TITLE)
        self.sound_background = GameImage(SOUND_BACKGROUND)
        self.sound_background.set_position(500 - self.sound_background.width / 2, 540)
        self.is_option = False

        self.sound_enable_button = ButtonClick(SOUND_ENABLE, self.window, 96, 600)
        self.sound_disabled_button = ButtonClick(SOUND_DISABLED, self.window, 96, 600)
        self.jogar_button = Button(self.window, 250, self.window.height - 96, "JOGAR")
        self.sair_button = Button(self.window, self.window.width - 250, self.window.height - 96, "SAIR")
        self.opcoes_button = Button(self.window, self.window.width / 2, self.window.height - 96, "OPÇÕES")
        self.voltar_button = Button(self.window, self.window.width - 250, 600, "VOLTAR")
        self.text = CenterText(window, 500, 600, color=GOLD, text="SONS E MÚSICAS")
        self.time = 0.0

    def handle_event(self, speed, state):
        self.time -= self.window.delta_time()
        if not self.is_option:
            if self.time > 0:
                return
            if self.jogar_button.is_button_pressed():
                self.window.main_scene.change_scene('FirstHistory')
            elif self.sair_button.is_button_pressed():
                pygame.display.quit()
                pygame.quit()
                exit()
            elif self.opcoes_button.is_button_pressed():
                self.is_option = not self.is_option
        else:
            if self.voltar_button.is_button_pressed():
                self.time = 0.5
                self.is_option = not self.is_option
            if self.window.sound.get_sound_state():
                if self.sound_enable_button.is_button_pressed():
                    self.window.sound.change_sound_state()
            elif not self.window.sound.get_sound_state():
                if self.sound_disabled_button.is_button_pressed():
                    self.window.sound.change_sound_state()

    def draw(self, state):
        self.fundo.draw()

        if not self.is_option:
            self.jogar_button.draw()
            self.sair_button.draw()
            self.opcoes_button.draw()
        else:
            self.voltar_button.draw()
            self.sound_background.draw()
            self.text.draw()
            if self.window.sound.get_sound_state():
                self.sound_enable_button.draw()
            else:
                self.sound_disabled_button.draw()

    def update(self, state):
        self.jogar_button.update()
        self.voltar_button.update()
        self.sair_button.update()
        self.opcoes_button.update()
