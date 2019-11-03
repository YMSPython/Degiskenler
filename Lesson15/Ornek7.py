from enum import Enum, unique


@unique
class Icecek(Enum):
    Vanilya = 7
    Çikolata = 4
    Vişne = 3
    Muzlu = 1
    Kiraz = 90


for x in Icecek:
    print(x)
    print("-" * 30)


for x, y in Icecek.__members__.items():
    print(x, y, y.value)
    print("-"*30)
