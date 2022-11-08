from pathlib import Path

from animals.animals import Deer
from animals.io import JSONIOAnimal, PickleIOAnimal

BASE_DIR = Path(__file__).resolve().parent

if __name__ == '__main__':
    deer = Deer(
        height=1.5,
        weight=40,
        color="beige"
    )
    io = PickleIOAnimal(str(BASE_DIR.joinpath('deer.pickle')))
    io.save(deer)

    print("Deer is saved")
    d2 = io.restore()
    print(d2)
