# Dışarıdan aldığı değere göre kare çizen metot


def kare_ciz_1(sayi):
    i = 0
    while i <= sayi:
        metin = ""
        for x in range(sayi + 5):
            metin += "X "
        print(metin)
        i += 1


kare_ciz_1(10)
print("-" * 30)


def kare_ciz_2(sayi):
    i = 0
    while i <= sayi:
        print("X " * (sayi + 5))
        i += 1


kare_ciz_2(10)

print("-" * 30)


def kare_ciz_3(sayi):
    for i in range(sayi + 1):
        print("X " * (sayi + 5))


kare_ciz_3(10)