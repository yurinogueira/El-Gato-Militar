from constants import FIRE_BALL_REVERSE
from src.itemgame.ItemModel import ItemModel
from src.itemgame.ShotModel import ShotModel


class ShotEnemyModel(ShotModel):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, FIRE_BALL_REVERSE)


    def move(self, fps: int):
        if fps > 0:
            delta_fps = 0.5 / fps
            delta_speed = 100 * fps
            if self.shotAnimation.x != 2000:
                self.shotAnimation.x -= int(delta_speed * delta_fps) / 5

            if self.shotAnimation.x < -self.shot.animation.width:
                self.shotAnimation.x = 2000