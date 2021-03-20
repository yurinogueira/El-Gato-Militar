from PPlay.gameimage import *
from constants import *
from src.interfaces.SceneInteface import SceneInterface
from src.model.CatModel import CatModel
from src.model.PowerUpModel import PowerUpModel


class HomeScene(SceneInterface):

    @staticmethod
    def __generate_points():
        powers = []
        for i in range(POINTS):
            powers.append(PowerUpModel())
        return powers

    def __init__(self, hud):
        self.hud = hud
        self.fundo = GameImage(BACKGROUND_HOME)
        self.cat = CatModel()
        self.speed = 0
        self.powers = self.__generate_points()
        self.hud.set_time(60)

    def handle_event(self, speed, event):
        self.speed = speed
        if event.key_pressed("UP"):  # Direcional ^
            self.cat.jump(300)
        elif event.key_pressed("LEFT"):
            self.cat.walk_fliped()
        elif event.key_pressed("RIGHT"):
            self.cat.walk()
        else:
            self.cat.idle()

    def draw(self):
        self.fundo.draw()
        self.cat.draw()
        self.hud.draw_with_time()

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
