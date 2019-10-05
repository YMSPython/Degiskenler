# Programcı Hataları (Error) (Bug)
# İstisnai Hatalar   (Exception)
# Mantıksal Hatalar

# print(int(input("Lütfen Telefon Numaranızı Giriniz : ")))


try:
    print(int(input("Telefon Numaranızı Giriniz : ")))
    sayi1 = 1
    sayi2 = 0
    sonuc = sayi1 / sayi2
except ValueError:
    # A Takımına
    print("Bir Telefon numarası girmek nekadar zor olabilir.")
except ZeroDivisionError:
    # B Takımına
    print("Sıfıra bölünme hatası bi kontrol et")