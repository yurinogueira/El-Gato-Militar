from abc import ABC, abstractmethod


class GameObjectInterface(ABC):

    @abstractmethod
    def draw(self): raise NotImplementedError

    @abstractmethod
    def update(self): raise NotImplementedError

    @abstractmethod
    def move(self, fps: int): raise NotImplementedError
