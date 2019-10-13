sehirler = ["adana", "ankara", "edirne", "urfa","amasya", "antep"]

# dizi içerisinde yer alan elemanların içerisinde(isminde) "m" harfi geçenleri ekrana yazdırınız.


for sehir in sehirler:
    if "m" in sehir:
        print(sehir)
    else:
        print(sehir, "ismi içerisinde \"m\" karakteri geçmemektedir.")