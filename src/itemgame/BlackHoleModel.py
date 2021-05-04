from PPlay.point import Point
from PPlay.sprite import Sprite
from constants import BLACK_HOLE
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ItemModel import ItemModel
from src.model.AirPlaneModel import AirPlaneModel


class BlackHoleModel(GameObjectInterface):
    def __init__(self, x: int, y: int):
        self.blackhole = ItemModel(BLACK_HOLE)
        self.blackholeAnimation = self.blackhole.animation
        self.blackholeAnimation.set_position(x, 20 )
        self.middle = self.blackhole.x + (self.blackholeAnimation.width / 2)

    def draw(self):
        self.blackholeAnimation.draw()

    def update(self):
        self.blackholeAnimation.update()

    def move(self, fps: int):
        pass

    def attraction(self, obj:AirPlaneModel):
        if obj.animation.x <= self.middle:
            obj.forward(0.1)
        elif obj.animation.x > self.middle:
            obj.backward(0.1)

        if obj.animation.y > self.y:
            obj.update(0.05)

