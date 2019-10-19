# Dışarıdan girilen 2 sayının toplamını ekrana yazdırma
# Kural 1) Kesinlike metot içerisine parametrenin nerden geleceği tanımlanmaz

# Kural 2) Kesinlike metot içerisinde parametreye değer atanmaz.


def Hesapla(sayi1, sayi2):
    #sayi1 = int(input("Lütfen 1. Sayıyı giriniz : "))
    #sayi2 = int(input("Lütfen 2. Sayıyı giriniz : "))
    #sayi1 = 15
    toplam = sayi1 + sayi2
    print(toplam)


Hesapla(10, 10)
Hesapla(int(input("Lütfen 1. sayıyı giriniz : ")),
        int(input("Lütfen 2. sayıyı giriniz : ")))

sonuc = ((10 * 10) - 20) / 5
Hesapla(sonuc, (sonuc * sonuc))
