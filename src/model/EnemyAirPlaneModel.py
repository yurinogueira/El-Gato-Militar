import random

from pplay.sprite import Sprite

from src.hud.LifeHud import EnemyLifeHud

from src.itemgame.ShotEnemyModel import ShotEnemyModel

from src.model.AirPlaneModel import AirPlaneModel

from constants import *


class EnemyAirPlaneModel(AirPlaneModel):
    def __init__(self, x, y):
        self.sprites = [PLUS_JET_ENEMY_PINK_FLY, PLUS_JET_ENEMY_GREEN_FLY,
                        PLUS_JET_ENEMY_YELLOW_FLY, PLUS_JET_ENEMY_RED_FLY]
        super().__init__(x, y, sprite=self.sprites[random.randint(0, 3)])
        self.move_plane = 0
        self.is_hidden = False
        self.time = 0
        self.lifeModel = EnemyLifeHud(x, y, LIFE_HUD_ENEMY, LIFE_POINTS_ENEMY)
        self.shotModel = ShotEnemyModel(2000, 2000)

    def backward(self, fps):
        self.animation.x += fps

    def forward(self, fps):
        self.animation.x -= fps

    def shot(self, shot=None):
        if self.shotModel.shotAnimation.x == 2000:
            shot_x = self.animation.x - 100
            shot_y = self.animation.y + (self.animation.height / 2)
            self.shotModel.set_position(shot_x, shot_y)

    def hidden(self):
        self.animation = Sprite(*self.sprites[random.randint(0, 3)])
        self.animation.set_loop(True)
        self.animation.set_total_duration(1000)
        self.animation.set_position(2000, 2000)
        self.is_hidden = True
        self.lifeModel.hidden()
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

    def can_shot(self, airplane: AirPlaneModel):
        if abs(self.animation.y - airplane.animation.y) < 150 and not self.is_hidden:
            PLANE_LASER_SHOTS.play()
            self.shot()

    def get_shot(self):
        return self.shotModel



