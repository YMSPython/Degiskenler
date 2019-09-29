# -*- coding: utf-8 -*-
# Degisken tanimlama kurallari
# 1) degisken, ismi sayi ile baslayamaz
# 2) degisken, 2 kelimeden olusamaz(ayrik)
# 3) degisken, ismi icerisinde sadece izin verilen ozel karakterler kullanilabilir(_)
# 4) degisken, tanimlamasi yapilirken, kesinlikle tanimli kelimeler kullanilmaz
# 5) degisken, ismi icerisinde turkce karakter kullanmayiniz.



benimAdim    = "Murat"
benimSoyadim = "Vuranok"

print(benimAdim)

# int      tam sayi
# string   metinsel
# float    ondaliki sayi
# boolean  True/False mantiksal veri tipi

sayi = 5
print("islem sonucu", sayi)

print(benimAdim)
print(benimSoyadim)
print(benimAdim + " " + benimSoyadim)

# + operatoru metinsel degerlerde birlestirme islemi yapar.

print(benimAdim, benimSoyadim)


isim     = "murat"
soyisim  = "vuranok"
fullname = isim + " " +soyisim

print("Kullanicinin Adi Soyadi : " ,         fullname       )

sayi1 = 10
sayi2 = 20

# c# => 8 tane tam sayi veri tipi mevcut (byte, sbyte,short,ushor,int, uint, long,ulong)
# python => 2 int, long



metin = "bilge\nadam"  #    \n bir alt satir(new line)
print(metin)

metin = """
bilge
adam
besiktas
python 
dersleri
"""

print (metin)



x = True
y = False


# (escape sequence) kacis karakteri

#      "bilge adam" besiktas subesi "python" dersleri


metin = "\"bilge adam\" besiktas subesi \"python\" dersleri"
print(metin)




metin = "\"bilge adam\" besiktas subesi \"python\" dersleri\n"
print(metin *5)  # metin degiskeninin ekrana 5 defa yazdirilmasi



result = 10 > 2   # True degerini teslim eder.
print(result)

















