import random

from constants import *
from src.hud.LifeHud import LifeHud
from src.itemgame.ShotEnemyModel import ShotEnemyModel
from src.model.AirPlaneModel import AirPlaneModel


class EnemyAirPlaneModel(AirPlaneModel):
    def __init__(self, x, y, sprite=PLUSJET_RED_FLY):
        super().__init__(x, y, sprite)
        self.move_plane = 0
        self.is_hidden = False
        self.time = 0
        self.lifeModel = LifeHud(x, y, LIFE_HUD_ENEMY, LIFE_POINTS_ENEMY)
        self.shotModel = ShotEnemyModel(2000, 2000)


    def backward(self, fps):
        self.animation.x += fps

    def forward(self, fps):
        self.animation.x -= fps

    def shot(self):
        if self.shotModel.shotAnimation.x == 2000:
            shot_x = self.animation.x - 100
            shot_y = self.animation.y + (self.animation.height / 2)
            self.shotModel.set_position(shot_x, shot_y)

    def hidden(self):
        self.animation.set_position(2000, 2000)
        self.is_hidden = True
        self.animation.y = random.randint(0, HEIGHT_SCREEN)
    
    def move(self, speed):
        movement = [self.up, self.down, self.backward, self.forward]
        if not self.is_hidden:
            self.time += 1
            if self.time % 60 == 0:
                self.move_plane = random.randint(0, len(movement)-1)
                self.time = 0
            else:
                if self.animation.x < WIDTH_SCREEN / 2:
                    self.move_plane = 2

                move_to = movement[self.move_plane]
                move_to(speed)

            super(EnemyAirPlaneModel, self).move(speed)
            self.lifeModel.move(self.animation.x + 15, self.animation.y - 15)

        else:
            self.forward(speed)
            if self.animation.x + self.animation.width < WIDTH_SCREEN:
                self.lifeModel.full_life()
                self.is_hidden = False

    def get_life(self):
        return self.lifeModel

    def can_shot(self, airplane:AirPlaneModel):
        if abs(self.animation.y - airplane.animation.y) < 150 and not self.is_hidden:
            self.shot()

    def get_shot(self):
        return self.shotModel



