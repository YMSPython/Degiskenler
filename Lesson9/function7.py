# dışarıdan girilen metin içerisinde yer alan türkçe karakterler veya özel karakterlerden arındıran bir metot yazınız.


# ÇAĞLAR.DERİN@BİLGEADAM.COM
# caglar.derin@bilgeadam.com

def DonguluReplace(string):
    metin = []
    ozelkarakterler = ['ş','ğ','ç','ö','ü','ı']
    karakterler =     ['s','g','c','o','u','i']

    for c in string:
        index = 0
        result = True
        for i in ozelkarakterler:
            if c == i:
                metin.append(karakterler[index])
                result = False
                break
            index += 1   # 5
        if result:
            metin.append(c)
    return metin

result = DonguluReplace("şğçöüıaabbğüişçö")
#print(result)
 


 

def Translator(entry):
    translationTable = str.maketrans("şğçıüö", "sgciuo")
    entry = entry.lower()
    entry = entry.translate({ord(['$']): None})
    entry = entry.translate(translationTable)
    return entry

print(Translator("Fıstıkçı$şa#h-ap@neğber.com"))