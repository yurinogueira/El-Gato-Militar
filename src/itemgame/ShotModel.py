from constants import *
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ItemModel import ItemModel


class ShotModel(GameObjectInterface):
    def __init__(self, x: int, y: int, sprite=FIRE_BALL):
        self.shot = ItemModel(sprite)
        self.shotAnimation = self.shot.animation
        self.shotAnimation.set_position(x, y)
        self.reloadShot = True

    def draw(self):
        self.shotAnimation.draw()

    def update(self):
        self.shotAnimation.update()

    def move(self, fps: int):
        if fps > 0:
            delta_fps = 0.5 / fps
            delta_speed = 100 * fps
            if self.shotAnimation.x != 2000:
                self.shotAnimation.x += int(delta_speed * delta_fps) / 5

            if self.shotAnimation.x > WIDTH_SCREEN:
                self.shotAnimation.x = 2000

    def collide(self, obj):
        return self.shot.collide(obj)

    def set_position(self, x: int, y: int):
        self.shotAnimation.x = x
        self.shotAnimation.y = y

    def is_hidden(self):
        return self.shotAnimation.x == 2000
