from abc import ABC, abstractmethod


class ShopObjectInterface(ABC):

    @abstractmethod
    def draw(self): raise NotImplementedError

    @abstractmethod
    def handle_event(self): raise NotImplementedError

    @abstractmethod
    def move(self, fps: int): raise NotImplementedError
