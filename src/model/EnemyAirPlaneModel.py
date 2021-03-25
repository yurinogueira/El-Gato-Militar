import random

from constants import *
from src.model.AirPlaneModel import AirPlaneModel


class EnemyAirPlaneModel(AirPlaneModel):
    def __init__(self, x, y, sprite=PLUSJET_RED_FLY):
        super().__init__( x, y, sprite)
        self.move_plane = 0
        self.target = False
        self.time = 0

    def backward(self, fps):
        self.animation.x += fps

    def forward(self, fps):
        self.animation.x -= fps

    def shot(self):
        if self.shotModel.shotAnimation.x == 2000:
            shot_x = self.animation.x - self.animation.width
            shot_y = self.animation.y - (self.animation.height / 2)
            self.shotModel.set_position(shot_x, shot_y)

    def hidden(self):
        self.animation.set_position(2000, 2000)
        self.target = True
        self.animation.y = random.randint(0, HEIGHT_SCREEN)
    
    def move(self, speed):
        movement = [self.up, self.down, self.backward, self.forward]
        if not self.target:
            self.time += 1
            if self.time % 60 == 0:
                self.move_plane = random.randint(0, len(movement)-1)
                self.time = 0
            else:
                func_arr = movement[self.move_plane]
                func_arr(speed)
            super(EnemyAirPlaneModel, self).move(speed)

        else:
            self.forward(speed)
            if self.animation.x + self.animation.width < WIDTH_SCREEN:
                self.target = False



