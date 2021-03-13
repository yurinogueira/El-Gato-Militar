from PPlay.sprite import Sprite
from src.factory.Points import Point
import constants as CONS


class CatModel:
    def __init__(self):
        self.ground_limit = CONS.GROUND
        self.animation = Sprite(*CONS.CAT_SPRITE_WALK)
        self.animation.set_total_duration(1000)
        self.animation.set_position(0, self.ground_limit)
        self.point = 0
        self.x = self.animation.x
        self.y = self.animation.y
        self.antx = 0
        self.anty = 0

    def jump(self, fps):
        if self.animation.y == self.ground_limit:
            self.__change_sprite(*CONS.CAT_SPRITE_JUMP, 500, False)
            self.animation.y -= fps

    def walk(self):
        self.__change_sprite(*CONS.CAT_SPRITE_WALK)

    def is_playing(self):
        return self.animation.is_playing()

    def move(self, speed):

        self.animation.move_key_y(speed)
        self.animation.move_key_x(speed)

        if self.animation.y < self.ground_limit:
            self.animation.y += speed * 5
        if self.animation.y > self.ground_limit:
            self.animation.y = self.ground_limit
        if self.animation.x + self.animation.width > CONS.WIDTH_SCREEN:
            self.animation.x = CONS.WIDTH_SCREEN - self.animation.width
        if self.animation.x < 0:
            self.animation.x = 0

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()

    def __change_sprite(self, path, frame, total_duration=1000, loop=True):
        self.x = self.animation.x
        self.y = self.animation.y
        self.animation = Sprite(path, frame)
        self.animation.x = self.x
        self.animation.y = self.y
        self.animation.set_total_duration(total_duration)
        self.animation.set_loop(loop)
