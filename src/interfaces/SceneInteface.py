from abc import ABC, abstractmethod


class SceneInterface(ABC):

    @abstractmethod
    def handle_event(self, speed: int, scene: bool): raise NotImplementedError

    @abstractmethod
    def draw(self, state: bool): raise NotImplementedError

    @abstractmethod
    def update(self, state: bool): raise NotImplementedError
