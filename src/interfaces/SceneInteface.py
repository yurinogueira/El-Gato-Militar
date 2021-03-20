from abc import ABC, abstractmethod

import PPlay


class SceneInterface(ABC):

    @abstractmethod
    def handle_event(self, speed: int, event: PPlay.keyboard.Keyboard): raise NotImplementedError

    @abstractmethod
    def draw(self): raise NotImplementedError

    @abstractmethod
    def update(self): raise NotImplementedError
