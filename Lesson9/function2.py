# Dışarıdan girilen değerin, tek veya cift olma durumuna göre geriye değer dönen metot, sayı cift ise : -1, tek ise : 1, sıfıra eşit ise : 0 değerini teslim etsin


def TekCiftKontrolu(sayi):
    if sayi == 0:
        return 0
    elif sayi % 2 == 0:
        return -1
    else:
        return 1


def TekCiftKontrolu_(sayi):
    result = 0
    if sayi == 0:
        result = 0
    elif sayi % 2 == 0:
        result = -1
    else:
        result = 1
    return result


result = TekCiftKontrolu(int(input("Lütfen bir sayı giriniz : ")))
print(result)
