from abc import ABC, abstractmethod


class AbstractAnimal(ABC):
    name = None

    def __init__(self, height, weight, color):
        self.height: float = height
        self.weight: float = weight
        self.color: str = color

    @abstractmethod
    def hunting_info(self):
        pass


class Deer(AbstractAnimal):
    name = "deer"

    def hunting_info(self):
        return "Use Big Calibre Rifle"


class Hare(AbstractAnimal):
    name = "hare"

    def hunting_info(self):
        return f"Use Warming rifle. Color of Hare is {self.color}"
