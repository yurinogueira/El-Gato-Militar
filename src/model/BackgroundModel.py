from pplay.sprite import Sprite

from src.interfaces.GameObjectInterface import GameObjectInterface


class BackgroundModel(GameObjectInterface):
    def __init__(self, sprite, x=0, y=0):
        self.x = x
        self.y = y
        self.background_1 = Sprite(sprite)
        self.background_1.set_total_duration(1000)
        self.background_1.set_position(x, y)

        self.background_2 = Sprite(sprite)
        self.background_2.set_total_duration(1000)
        self.background_2.set_position(self.background_1.width, y)

    def draw(self):
        self.background_1.draw()
        self.background_2.draw()

    def update(self):

        self.background_1.update()
        self.background_2.update()

    def move(self, fps: int):
        self.background_1.set_position(self.background_1.x - fps, self.y)
        self.background_2.set_position(self.background_2.x - fps, self.y)

        if self.background_1.x < -self.background_1.width:
            self.background_1.x = self.background_1.width
        if self.background_2.x < -self.background_2.width:
            self.background_2.x = self.background_2.width
        if self.background_1.x > 0:
            self.background_2.x = -self.background_2.width + self.background_1.x
        if self.background_2.x > 0:
            self.background_1.x = -self.background_1.width + self.background_2.x

