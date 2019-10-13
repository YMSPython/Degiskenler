metin = input("Lütfen bir metin giriniz : ").lower()
sesli_harfler = ['a', 'e', 'i', 'ı', 'o', 'ö', 'u', 'ü']
sesli = []
sessiz = []
i = 0

while i < len(metin): #sakeğpwqeğıwqewjlamd
    result = True
    y = 0
    while y < len(sesli_harfler): 
        if metin[i] == sesli_harfler[y]:
            sesli.append(metin[i])
            result = False
            break
        y += 1

    if result:
        sessiz.append(metin[i]) 
    i += 1


print("Metin içerisinde toplamda sesli harf sayısı : {}\nMetin içerisinde toplamda sessiz harf sayısı : {}".format(
    len(sesli), len(sessiz)))