from PPlay.gameimage import *
import pygame
from constants import *
from src.factory.Button import Button
from src.interfaces.SceneInteface import SceneInterface


class MenuScene(SceneInterface):

    def __init__(self, hud):
        self.hud = hud
        self.window = hud.get_window()
        self.fundo = GameImage(BACKGROUND_HOME)
        self.jogar_button = Button(self.window, 250, self.window.height - 96, "JOGAR")
        self.sair_button = Button(self.window, self.window.width - 250, self.window.height - 96, "SAIR")

    def handle_event(self, speed, event, state):
        if self.jogar_button.is_button_pressed():
            import teste
            teste.change_scene('Home')
        elif self.sair_button.is_button_pressed():
            pygame.display.quit()
            pygame.quit()

    def draw(self, state):
        self.fundo.draw()
        self.jogar_button.draw()
        self.sair_button.draw()

    def update(self, state):
        self.jogar_button.update()
