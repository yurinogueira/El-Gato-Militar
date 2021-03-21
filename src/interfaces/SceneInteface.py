from abc import ABC, abstractmethod

import PPlay


class SceneInterface(ABC):

    @abstractmethod
    def handle_event(self, speed: int, event: PPlay.keyboard.Keyboard, scene: bool): raise NotImplementedError

    @abstractmethod
    def draw(self, state: bool): raise NotImplementedError

    @abstractmethod
    def update(self, state: bool): raise NotImplementedError
