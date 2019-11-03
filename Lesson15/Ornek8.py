from enum import Enum, unique, auto


@unique
class Icecek(Enum):
    Vanilya = auto()
    Çikolata = 6
    Vişne = auto()
    Muzlu = auto()
    Kiraz = auto()


for x, y in Icecek.__members__.items():
    print(x, y, y.value)
    print("-"*30)


liste = list(Icecek)
print(liste)