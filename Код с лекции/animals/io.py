import json
import pickle

from abc import ABC, abstractmethod

from animals.animals import AbstractAnimal, Deer, Hare


class AbstractIOAnimal(ABC):

    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def save(self, animal: AbstractAnimal):
        pass

    @abstractmethod
    def restore(self) -> AbstractAnimal:
        pass


class JSONIOAnimal(AbstractIOAnimal):

    def save(self, animal: AbstractAnimal):
        with open(self.filepath, 'w') as f:
            json.dump({
                'height': animal.height,
                'weight': animal.weight,
                'color': animal.color,
                'class_name': animal.name
            }, f, indent=4)

    def restore(self) -> AbstractAnimal:
        with open(self.filepath, 'r') as f:
            content: dict = json.load(f)

            match content.pop('class_name'):
                case Deer.name:
                    return Deer(**content)
                case Hare.name:
                    return Hare(**content)

class PickleIOAnimal(AbstractIOAnimal):

    def save(self, animal: AbstractAnimal):
        with open(self.filepath, 'wb') as f:
            pickle.dump(animal, f)

    def restore(self) -> AbstractAnimal:
        with open(self.filepath, 'rb') as f:
            return pickle.load(f)
