import pygame

from PPlay import mouse
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite

from src.factory.Hud import HudManager
from src.factory.Text import CenterText
from src.interfaces.SceneInteface import SceneInterface

from constants import *


class SelectPlaneScene(SceneInterface):
    def __init__(self, hud: HudManager):
        self.hud = hud
        self.window = hud.get_window()
        self.mouse = hud.get_window().get_mouse()
        self.fundo = GameImage(BACKGROUND_HOME)
        self.time = 0
        self.select = False
        points_background = pygame.transform.scale(GameImage(SOUND_BACKGROUND).image, (1100, 800))
        self.point_background = GameImage(SOUND_BACKGROUND)
        self.point_background.image = points_background
        self.point_background.set_position(self.window.width / 2 - points_background.get_width() / 2, 0)

        self.text = CenterText(hud.get_window(), WIDTH_DIV, 300,
                               text="Escolha qual será sua próxima nave")

        self.jet_g_bool = False
        self.jet_green = Sprite(*JET_GREEN_FLY)
        self.jet_green.set_position(WIDTH_DIV - WIDTH_DIV / 2 - self.jet_green.width + 200, 350)

        self.jet_y_bool = False
        self.jet_yellow = Sprite(*JET_YELLOW_FLY)
        self.jet_yellow.set_position(WIDTH_DIV + WIDTH_DIV / 2 - 200, 350)

    def handle_event(self, speed: int, scene: bool):
        if self.mouse.is_over_object(self.jet_green):
            self.jet_g_bool = True
            self.jet_y_bool = False
            if self.mouse.is_button_pressed(mouse.BUTTON_LEFT):
                self.hud.set_ship_look(JET_GREEN_FLY)
                self.select = True
        elif self.mouse.is_over_object(self.jet_yellow):
            self.jet_y_bool = True
            self.jet_g_bool = False
            if self.mouse.is_button_pressed(mouse.BUTTON_LEFT):
                self.hud.set_ship_look(JET_YELLOW_FLY)
                self.select = True
        else:
            self.time = 2
            self.jet_g_bool = False
            self.jet_y_bool = False

    def __draw_jet(self, jet: Sprite, enabled: bool):
        if enabled:
            if self.time >= 0.0:
                self.time -= self.window.delta_time()
            if 1.7 <= self.time <= 2.0:
                jet.draw()
            elif 1.1 <= self.time <= 1.4:
                jet.draw()
            elif 0.5 <= self.time <= 0.8:
                jet.draw()
            elif self.time <= 0.0:
                jet.draw()
        else:
            jet.draw()

    def draw(self, state: bool):
        self.fundo.draw()
        self.point_background.draw()
        self.__draw_jet(self.jet_yellow, self.jet_y_bool)
        self.__draw_jet(self.jet_green, self.jet_g_bool)
        self.text.draw()

    def update(self, state: bool):
        if self.select:
            self.window.main_scene.change_scene('Desert')
