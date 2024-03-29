from pplay.sprite import Sprite

from src.interfaces.GameObjectInterface import GameObjectInterface

from constants import *


class CatModel(GameObjectInterface):
    def __init__(self):
        self.ground_limit = GROUND
        self.animation = Sprite(*CAT_SPRITE_IDLE)
        self.animation.set_loop(False)
        self.animation.set_total_duration(1000)
        self.animation.set_position(0, self.ground_limit)
        self.x = self.animation.x
        self.y = self.animation.y
        self.point = 0
        self.antx = 0
        self.anty = 0
        self.looking_to = True
        self.jumping = False
        self.original_y = 0

    def jump(self):
        if self.animation.y == self.ground_limit:
            self.__set_sprite(CAT_SPRITE_JUMP, CAT_SPRITE_JUMP_FLIPED, self.looking_to, 500)
            self.original_y = self.animation.y
            self.jumping = True

    def idle(self):
        if self.animation.total_duration == 980 or self.animation.total_duration == 970:
            self.__set_sprite(CAT_SPRITE_IDLE, CAT_SPRITE_IDLE_FLIPED, self.looking_to, 1000)
        elif not self.is_playing():
            self.__set_sprite(CAT_SPRITE_IDLE, CAT_SPRITE_IDLE_FLIPED, self.looking_to, 1000)

    def walk(self):
        if self.animation.total_duration == 1000 or self.animation.total_duration == 970:
            self.__set_sprite(CAT_SPRITE_WALK, CAT_SPRITE_WALK_FLIPED, True, 980)
        elif not self.is_playing():
            self.__set_sprite(CAT_SPRITE_WALK, CAT_SPRITE_WALK_FLIPED, True, 980)

    def walk_fliped(self):
        if self.animation.total_duration == 1000 or self.animation.total_duration == 980:
            self.__set_sprite(CAT_SPRITE_WALK, CAT_SPRITE_WALK_FLIPED, False, 970)
        elif not self.is_playing():
            self.__set_sprite(CAT_SPRITE_WALK, CAT_SPRITE_WALK_FLIPED, False, 970)

    def is_playing(self):
        return self.animation.is_playing()

    def move(self, speed):
        if self.jumping:
            self.animation.move_key_y(speed)
        self.animation.move_key_x(speed)

        if self.animation.y < self.ground_limit:
            self.animation.y += speed * 1.8
        if self.animation.y > self.ground_limit:
            self.animation.y = self.ground_limit
        if self.animation.x + self.animation.width > WIDTH_SCREEN:
            self.animation.x = WIDTH_SCREEN - self.animation.width
        if self.animation.x < 0:
            self.animation.x = 0

    def draw(self):
        self.animation.draw()

    def update(self):
        if self.jumping:
            self.y -= 2
            self.animation.y = self.y
            if self.original_y - self.y >= JUMP_MAX:
                self.__set_sprite(CAT_SPRITE_FALL, CAT_SPRITE_FALL_FLIPED, self.looking_to, 500)
                self.jumping = False
        self.animation.update()

    def __set_sprite(self, sprite, sprite_fliped, looking_to, duration=980):
        self.looking_to = looking_to
        if self.looking_to:
            self.__change_sprite(*sprite, total_duration=duration, loop=False)
        else:
            self.__change_sprite(*sprite_fliped, total_duration=duration, loop=False)

    def __change_sprite(self, path, frame, total_duration=980, loop=True):
        self.x = self.animation.x
        self.y = self.animation.y
        self.animation = Sprite(path, frame)
        self.animation.x = self.x
        self.animation.y = self.y
        self.animation.set_total_duration(total_duration)
        self.animation.set_loop(loop)
