try:
    sayi_bir = int(input("Lütfen birinci sayıyı giriniz : "))
    number_2 = int(input("Lütfen ikinci sayıyı giriniz : "))

    toplam = sayi_bir + number_2
    fark   = sayi_bir - number_2
    bolum  = sayi_bir / number_2
    carpim = sayi_bir * number_2

 #   print("Sayıların Toplamı :",toplam)
 #   print("Sayıların Farkı : "+ str(fark))
 #   print("Sayıların Toplamı :",toplam,"\nSayıların Farkı :",fark)
    print("Sayıların Toplamı : {}\nSayıların Farkı : {}\nSayıların Çarpımı : {}\nSayıların Bölümü : {}".format(toplam,fark,carpim,bolum))

except (ValueError,SyntaxError):
     print("ValueError veya SyntaxError Hatası")
except ZeroDivisionError:
     pass
except FileExistsError:
     pass
except:
    pass
 
 

 