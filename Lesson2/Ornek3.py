# Hata mesajı

try:
    sayi = int(input("Lütfen sadece sayısal veri giriniz : "))
    print("Gelen Sayı : ", sayi)
    sayi = sayi / 0
    sayi = str(sayi) /0
    print("İşlem sonu")
except ValueError as hata:
    print("Beklenmedik bir hata ile karşılaşıldı!\nLütfen Tekrar Deneyiniz!")
    print("Sistem hata mesajı ",hata) # log dosyasına eklenecek
except ZeroDivisionError as hata:
    print("Sıfıra Bölme Hatası")
