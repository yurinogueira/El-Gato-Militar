
from PPlay.gameimage import *
from src.model.CatModel import CatModel
import constants as CONST
from src.model.PowerUpModel import PowerUpModel


class HomeScene:

    def __init__(self):
        self.fundo = GameImage(CONST.BACKGROUND_HOME)
        self.cat = CatModel()
        self.speed = 0
        self.points = 0
        self.powers = self.__generatePoints()

    def handle_event(self, speed, event ):
        self.speed = speed
        if event.key_pressed("UP"):# Direcional ^
            self.cat.jump(300)
        # elif key_board.key_pressed("DOWN"):  # Direcional \/
        #     print("Baixo!")
        # elif key_board.key_pressed("LEFT"):  # Direcional
        #     print("Direita!")
        elif not self.cat.is_playing():
            self.cat.walk()


    def draw(self):
        self.fundo.draw()
        self.cat.draw()


    def update(self):
        self.points += self.__spawn_points()
        self.cat.move(self.speed)
        self.cat.update()

    def __generatePoints(self):
        powers = []
        for i in range(CONST.POINTS):
            powers.append(PowerUpModel())
        return powers

    def __spawn_points(self):
        temp_points = 0

        for p in self.powers:
            p.move(self.speed)
            p.draw()
            temp_points += p.collide(self.cat)
            p.update()

        return temp_points





