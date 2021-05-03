from PPlay.sprite import Sprite
from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ShotModel import ShotModel


class AirPlaneModel(GameObjectInterface):

    def __init__(self, x=300, y=HEIGHT_SCREEN / 2, sprite=JET_BLUE_FLY, shoot=FIRE_BALL_BLUE):
        self.animation = Sprite(*sprite)
        self.animation.set_loop(True)
        self.animation.set_total_duration(1000)
        self.animation.set_position(x, y)
        self.ground_limit = HEIGHT_SCREEN - self.animation.height
        self.shotModel = ShotModel(2000, 2000)
        self.shotModel_special = ShotModel(2000, 2000, shoot)

    def set_special_look(self, sprite: Sprite):
        self.shotModel_special.shot.animation = sprite

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()

    def move(self, speed):
        if self.animation.y < 20:
            self.animation.y = 20
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

    def shot(self, shot=None):
        PLANE_LASER_SHOTS.play()
        if shot is None:
            shot = self.shotModel
        if shot.shotAnimation.x == 2000:
            shot_x = self.animation.x + self.animation.width
            shot_y = self.animation.y + (self.animation.height / 2)
            shot.set_position(shot_x, shot_y)

    def get_shot(self):
        return self.shotModel

    def get_shot_special(self):
        return self.shotModel_special

    def shot_special(self):
        self.shot(self.shotModel_special)
