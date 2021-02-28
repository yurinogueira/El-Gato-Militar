from PPlay.sprite import Sprite
import constants as CONS


class CatModel:
    def __init__(self):
        self.animation = Sprite(*CONS.CAT_SPRITE_WALK)
        self.animation.set_total_duration(1000)
        self.x = self.animation.x
        self.y = self.animation.y

    def jump(self):
        self.__change_sprite(*CONS.CAT_SPRITE_JUMP)
        self.animation.set_total_duration(500)
        self.animation.set_loop(False)

    def walk(self):
        self.__change_sprite(*CONS.CAT_SPRITE_WALK)
        self.animation.set_total_duration(1000)

    def is_playing(self):
        return self.animation.is_playing()

    def move(self, speed):
        self.animation.move_key_y(speed)
        self.animation.move_key_x(speed)

    def draw(self):
        self.animation.draw()

    def update(self):
        self.animation.update()

    def __change_sprite(self, path, size):
        self.x = self.animation.x
        self.y = self.animation.y
        self.animation = Sprite(path, size)
        self.animation.x = self.x
        self.animation.y = self.y
