from PPlay.sprite import Sprite
from constants import *


class AirPlaneModel:

    def __init__(self):
        self.animation = Sprite(*JET_BLUE_FLY)
        self.animation.set_loop(True)
        self.animation.set_total_duration(1000)
        self.animation.set_position(0, HEIGHT_SCREEN / 2)
        self.x = self.animation.x
        self.y = self.animation.y
        self.ground_limit = HEIGHT_SCREEN - self.animation.height
        self.point = 0
        self.antx = 0
        self.anty = 0
        self.looking_to = True

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()

    def up(self, fps):
        self.animation.y -= fps

    def down(self, fps):
        self.animation.y += fps

    def backward(self, fps):
        self.animation.x -= fps

    def forward(self, fps):
        self.animation.x += fps

    def move(self, speed):
        self.animation.move_key_y(speed)
        self.animation.move_key_x(speed)

        if self.animation.y < 0:
            self.animation.y = 0
        if self.animation.y > self.ground_limit:
            self.animation.y = self.ground_limit
        if self.animation.x + self.animation.width > WIDTH_SCREEN:
            self.animation.x = WIDTH_SCREEN - self.animation.width
        if self.animation.x < 0:
            self.animation.x = 0

