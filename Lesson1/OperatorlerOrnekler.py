# Örnek 1) Disaridan alinan
# iki sayının toplamiyla farkinin birbirine bolumunden kalanin sonucu kactir?

sayi1   = int(input("Lütfen birinci sayiyi giriniz : "))
sayi2   = int(input("Lütfen ikinci sayiyi giriniz : "))
toplam  = sayi1 + sayi2
fark    = sayi1 - sayi2
mod     = toplam % fark
print("Islem sonucu :", mod)


# Örnek 2) Disaridan girilen bir sayının 10 eksiginin 20 fazlasinin
# 2ye bolumunden kalaninin karesi kactir?



sayi3 = int(input("Lütfen bir sayi giriniz :"))

sonuc =  ((sayi3 - 10  + 20) % 2 ) ** 2
print(sonuc)

# Örnek 3) Disaridan girilen iki sayının karelerinin toplami
# ile karelerinin farki toplami kactir?




sayi4 = int(input("Lütfen birinci sayiyi giriniz :"))
sayi5 = int(input("Lütfen ikinci sayiyi giriniz : "))


kare1 = sayi4 * sayi4
kare2 = sayi5 * sayi5

kare3 = sayi4 **2
kare4 = sayi5 **2

toplam = kare1 + kare2
fark = kare1 - kare2
sonuc = toplam + fark
print("islem sonucu :", sonuc)




# Örnek 4) Vize notu'nun % 30'u, final notu'nun % 70'ini alıp öğrencinin not ortalamasini
#cikartan bir uygulama yaziniz...

final = float(input("Lütfen Final Notunuzu Giriniz : "))
vize  = float(input("Lütfen Vize Notunuzu Giriniz : "))
not_ortalamasi   = (vize * 0.30) + (final * 0.70)
print("Not ortalamanız :", not_ortalamasi)




# Örnek 5) Kullanıcı ilk Adını, 2. Olarak Soyadını girsin ve kullanıcıya mesaj olarak
# isim.soyisim@hotmail.com








ondalikli_sayi = 14.1111111111
print(round(ondalikli_sayi,7))  # virgulden sonraki haneyi belirlemek için kullaniriz.


isim = input("Lütfen adınız giriniz : ")
soyisim = input("Lütfen soyadınız giriniz : ")

mail = isim + "."+ soyisim+"@hotmail.com"

print(mail)



                     # murat.vuranok@bilgeadam.com



















