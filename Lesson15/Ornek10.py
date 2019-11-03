from enum import Enum, unique, auto, Flag


class Renkler(Flag):         
    Kırmızı = auto()  # 1
    Sarı = auto()     # 2
    Mavi = auto()     # 3
    Yeşil = auto()    # 4
    Pembe = auto()    # 5
    Turuncu = auto()  # 6
    Beyaz = Kırmızı | Mavi | Sarı


print((Renkler.Mavi and Renkler.Turuncu))
print(Renkler.Beyaz)

for x, y in Renkler.__members__.items():
    print(x,  y.value)
    print("-"*30)
