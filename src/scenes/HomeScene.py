from PPlay.gameimage import *
from constants import *
from src.model.CatModel import CatModel
from src.model.PowerUpModel import PowerUpModel


class HomeScene:

    @staticmethod
    def __generatePoints():
        powers = []
        for i in range(POINTS):
            powers.append(PowerUpModel())
        return powers

    def __init__(self, hud):
        self.hud = hud
        self.fundo = GameImage(BACKGROUND_HOME)
        self.cat = CatModel()
        self.speed = 0
        self.powers = self.__generatePoints()
        self.hud.set_time(60)

    def handle_event(self, speed, event):
        self.speed = speed
        if event.key_pressed("UP"):  # Direcional ^
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
        self.hud.points_hud()
        self.hud.time_hud('Battle')

        # A partir daqui é somente testes
        self.hud.life_hud(2)
        self.hud.special_hud(1)

    def update(self):
        self.hud.add_points(self.__spawn_points())
        self.cat.move(self.speed)
        self.cat.update()

    def __spawn_points(self):
        temp_points = 0

        for p in self.powers:
            p.move(self.speed)
            p.draw()
            temp_points += p.collide(self.cat)
            p.update()

        return temp_points
