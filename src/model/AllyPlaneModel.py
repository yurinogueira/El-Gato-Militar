import random

from constants import *
from src.model.EnemyAirPlaneModel import EnemyAirPlaneModel


class AllyPlaneModel(EnemyAirPlaneModel):
    def __init__(self, x, y, sprite=PLANE_PINK_FLY):
        super().__init__(x, y, sprite)

    def move(self, speed):
        movement = [self.up, self.down, self.backward, self.forward]
        if not self.is_hidden:
            self.time += 1
            if self.time % 60 == 0:
                self.move_plane = random.randint(0, len(movement)-1)
                self.time = 0
            else:
                if self.animation.x > WIDTH_SCREEN / 2:
                    self.move_plane = 3

                move_to = movement[self.move_plane]
                move_to(speed)

            super(EnemyAirPlaneModel, self).move(speed)
            self.lifeModel.move(self.animation.x + 15, self.animation.y - 15)

        else:
            self.forward(speed)
            if self.animation.x + self.animation.width < WIDTH_SCREEN:
                self.lifeModel.full_life()
                self.is_hidden = False
