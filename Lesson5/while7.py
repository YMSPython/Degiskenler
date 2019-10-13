dizi = [1, 2, 3, 4, 5, 6, 7,34,43,3,44231,123,3243,56,67, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# yukarıda yer alan dizinin içerisindeki elemanları tek ve cift olma durumuna göre ayrı dizilere ekleyiniz ve dizinin eleman adedlerini kullanıcıya bildiriniz.

i = 0
tek = []
cift =  []

while  i < len(dizi):
    if dizi[i] % 2 == 0:
        cift.append(dizi[i])
    else:
        tek.append(dizi[i])
    i += 1

print("Tek sayıların toplam adedi : {}\nÇift sayıların toplam adedi : {}".format(len(tek), len(cift)))

