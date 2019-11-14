from abc import ABC, abstractmethod


class SceneBase(ABC):

    def __init__(self, hero):
        self.hero = hero

    @abstractmethod
    def draw(self, sc):
        pass

    @abstractmethod
    def update(self, keys):
        pass