  
# Disaridan bir sayısal dizisinin parametre olarak alan bir metot yaziniz. Metot, parametredeki dizide yer alan elemanlarin toplaminin karekökünü dondursun...


# math kütüphanesinden yararlanabilirsiniz 

import math

def KareKokHesapla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return math.sqrt(toplam)
 
numbers = [1,2,3,4,5,6,7,8,9,112,22,33,44,55,66,77]

result = KareKokHesapla(numbers)
print("İşlem sonucu :", result)

# İşlem sonucu : 21.307275752662516