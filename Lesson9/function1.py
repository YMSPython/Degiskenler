# Dışarıdan aldığı değerlerin toplamını geriye dönen metot
# metot içerisinde yer alan return anahtar kelimesi önünde yer alan veriyi geriye teslim eder.
# return anahtar kelimesi, en sonda yer almalıdır. return'den sonra yazmayı deneyeceğiniz herşe boşa çaba harcamaktır. returnden sonra hiç bir kod  bloğu çalışmaz.


def Hesapla(s1, s2):
    return s1 + s2
    print("bu alanda yer kod bloğu çalışmaz!!")


result = Hesapla(5, 5)
print(result)
print(Hesapla(5, 5))
