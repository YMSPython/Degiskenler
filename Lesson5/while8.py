# dışarıdan girilen metin içerisinde yer alan sessli ve sessiz karakterleri ayrıştırınız ve kullanıcıya metin içerisinde kaç adet sessli, kaç adet sessiz harf var mesaj veriniz.

metin = input("Lütfen bir metin giriniz : ").lower()
sesli_harfler = ['a', 'e', 'i', 'ı', 'o', 'ö', 'u', 'ü']
sesli = []
sessiz = []
i = 0

while i < len(metin):
    adet  = sesli_harfler.count(metin[i])
    if sesli_harfler.count(metin[i]):
        sesli.append(metin[i])
    else:
        sessiz.append(metin[i])
    i += 1


print("Metin içerisinde toplamda sesli harf sayısı : {}\nMetin içerisinde toplamda sessiz harf sayısı : {}".format(
    len(sesli), len(sessiz)))
