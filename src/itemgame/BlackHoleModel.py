from PPlay.point import Point
from PPlay.sprite import Sprite
from PPlay.window import Window
from constants import BLACK_HOLE
from src.interfaces.GameObjectInterface import GameObjectInterface
from src.itemgame.ItemModel import ItemModel
from src.model.AirPlaneModel import AirPlaneModel


class BlackHoleModel(GameObjectInterface):
    def __init__(self, x: int, y: int):
        self.blackhole = ItemModel(BLACK_HOLE)
        self.blackholeAnimation = self.blackhole.animation

        self.blackholeAnimation.set_position(x, 20)
        self.middle = self.blackholeAnimation.x + (self.blackholeAnimation.width / 2)

    def draw(self):
        self.blackholeAnimation.draw()

    def update(self):
        self.blackholeAnimation.update()

    def move(self, fps: int):
        pass

    def collide(self, obj: AirPlaneModel):
        return self.blackhole.collide(obj)

    def attraction(self, speed, obj: AirPlaneModel):
        G = speed * 0.4
        if int(obj.animation.x) <= int(self.middle):
            obj.forward(G)
        elif int(obj.animation.x) > int(self.middle):
            obj.backward(G)

        if obj.animation.y > self.blackholeAnimation.y:
            obj.up(G)

