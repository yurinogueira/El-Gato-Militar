from PPlay.sprite import Sprite
from src.interfaces.GameObjectInterface import GameObjectInterface

class BackgroundModel(GameObjectInterface):
    def __init__(self, sprite):
        self.background_1 = Sprite(sprite)
        self.background_1.set_total_duration(1000)
        self.background_1.set_position(0, 0)

        self.background_2 = Sprite(sprite)
        self.background_2.set_total_duration(1000)
        self.background_2.set_position(self.background_1.width, 0)

    def draw(self):
        self.background_1.draw()
        self.background_2.draw()

    def update(self):

        self.background_1.update()
        self.background_2.update()

    def move(self, fps: int):
        self.background_1.set_position(self.background_1.x - fps, 0)
        self.background_2.set_position(self.background_2.x - fps, 0)

        if self.background_1.x < -self.background_1.width:
            self.background_1.x = self.background_1.width
        if self.background_2.x < -self.background_2.width:
            self.background_2.x = self.background_2.width

