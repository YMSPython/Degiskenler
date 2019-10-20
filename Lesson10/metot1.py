# Dışarıdan gelecek olan parametre sayısı belirsiz olan durumlar için kullanılan metot örneği
# C# => params
def Hesapla(*sayilar) -> float:
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

result = Hesapla(1,2,3,3,3,3,3,3,3,4,3,3,3 )
print(result)