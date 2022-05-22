from pplay.sprite import Sprite


class ItemModel:
    def __init__(self, *sprite, x=0, y=0):
        self.animation = Sprite(*sprite[0])
        self.animation.set_total_duration(1000)
        self.__setPosition_x = x
        self.__setPosition_y = y
        self.animation.set_position(self.__setPosition_x, self.__setPosition_y)
        self.x = self.animation.x
        self.y = self.animation.y
        self.collided = False

    def collide(self, obj):
        self.collided = False

        if self.animation.collided_perfect(obj.animation):
            self.animation.set_position(2000, 2000)
            self.collided = True

        return self.collided


class WindAnimation(Sprite):
    def __init__(self, image_file):
        super().__init__(*image_file)

    def move(self, speed):
        pass
