from PPlay.sprite import Sprite
from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ShotModel import ShotModel


class AirPlaneModel(GameObjectInterface):

    def __init__(self, x=300, y=HEIGHT_SCREEN / 2, sprite=JET_BLUE_FLY):
        self.animation = Sprite(*sprite)
        self.animation.set_loop(True)
        self.animation.set_total_duration(1000)
        self.animation.set_position(x, y)
        self.ground_limit = HEIGHT_SCREEN - self.animation.height
        self.shotModel = ShotModel(2000, 2000)

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()

    def move(self, speed):
        if self.animation.y < 0:
            self.animation.y = 0
        if self.animation.y > self.ground_limit:
            self.animation.y = self.ground_limit
        if self.animation.x + self.animation.width > WIDTH_SCREEN:
            self.animation.x = WIDTH_SCREEN - self.animation.width
        if self.animation.x < 0:
            self.animation.x = 0

    def up(self, fps):
        self.animation.y -= fps

    def down(self, fps):
        self.animation.y += fps

    def backward(self, fps):
        self.animation.x -= fps

    def forward(self, fps):
        self.animation.x += fps

    def shot(self):
        if self.shotModel.shotAnimation.x == 2000:
            shot_x = self.animation.x + self.animation.width
            shot_y = self.animation.y + (self.animation.height / 2)
            self.shotModel.set_position(shot_x, shot_y)

    def get_shot(self):
        return self.shotModel
