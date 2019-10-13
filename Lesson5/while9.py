metin = input("Lütfen bir metin giriniz : ").lower()
#sesli_harfler = ['a', 'e', 'i', 'ı', 'o', 'ö', 'u', 'ü']
sesli = []
sessiz = []
i = 0

while i < len(metin):
    if metin[i] == "a" or metin[i] == "e" or metin[i] == "ü" or metin[i] == "u" or metin[i] == "o" or metin[i] == "ö" or metin[i] == "ı" or metin[i] == "i":
        sesli.append(metin[i])
    else:
        sessiz.append(metin[i])

    i += 1


print("Metin içerisinde toplamda sesli harf sayısı : {}\nMetin içerisinde toplamda sessiz harf sayısı : {}".format(
    len(sesli), len(sessiz)))
