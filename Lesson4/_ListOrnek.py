# append() => dizi içerisine eleman eklemek için kullanılır.(javascript içinde aynı yöntem geçerlidir.)

# .append() => ekleme işlemine dizinin sonundan başlar, eklenen her bi eleman dizinin en son elemanıdır.

sehirler = []  # ['Ankara','Eskişehir','Adana','Bursa',x]
sehirler.append('Ankara')    # 0
sehirler.append('Eskişehir') # 1
sehirler.append('Adana')     # 2
sehirler.append('Bursa')     # 3

print(sehirler[:])

# .insert(item) => dizi içerisinde belirli bir aralığa eleman eklemek için kullanılır.

sehirler.insert(0,"Sivas")
print(sehirler[:])

# 1. Parametre hangi index değerine (int tipinde)
# 2. Parametre 1. Parametrede verilen index değerine karşılık gelecek olan veri (object)(gelecek olan veri tipi bilinmediğinden, object olarak değer ister.)

#--------------------------------------------------------------

#.pop() => dizi içerisinden eleman silme işlemi, parametre verilirse, verilen index değerindeki elemanı siler. parametre verilmez ise, dizinin en son elemanını siler.


# .pop() => metodun özelliği, silinen elemanı geriye teslim eder.
print(sehirler[:])
# ['Sivas', 'Ankara', 'Eskişehir', 'Adana', 'Bursa']
silinen_eleman = sehirler.pop() # => geriye Bursa şehrini teslim edecektir.
print(silinen_eleman)  

silinen_eleman = sehirler.pop(0) # => geriye Sivas şehrini teslim edecektir.
print(silinen_eleman)


# ------------------------------------------------
# .remove()  => dizi içerisinde eleman silme, eleman silmek için object olarak sizden parametre ister. (pop metodu index mantığı ile , remove metodu ise object mantığı ile çalışır)

# .remove() => metodu, geriye silinene elemanı teslim etmez
print(sehirler[:])
print(sehirler.remove('Eskişehir'))
print(sehirler[:])




# --------------------------------------------------

sehirler.append('Ankara')     
sehirler.append('Eskişehir')  
sehirler.append('Adana')     
sehirler.append('Bursa')     

# .sort() => dizinin elemanlarını A'dan Z'ye - 0'dan 9'a sıralama işlemi yapar.
#print(sehirler[:])
#sehirler.sort()
#print(sehirler[:])


# ---------------------------------------------
# .reverse() =>  sıralama yapmadan, diziyi tersine çevirir.

print(sehirler[:])
#sehirler.sort()
sehirler.reverse() 
print(sehirler[:])

#['Ankara', 'Adana', 'Ankara', 'Eskişehir', 'Adana', 'Bursa']
#['Bursa', 'Adana', 'Eskişehir', 'Ankara', 'Adana', 'Ankara']

# ---------------------------------------------
# len() => dizinin eleman sayısını(uzunluğu) teslim eder.

print(len(sehirler)) # Toplam dizinin eleman sayısı => 6
# (len(sehirler) - 1) => dizinin en son index değerini teslim eder.
# bir dizinin maximum index değeri, o dizinin eleman sayısının -1 değeridir.


#del sehirler
#print(len(sehirler))
#print(sehirler[:]) # NameError: name 'sehirler' is not defined
# del => anahtar kelimesi,   önüne tanımlanan nesneyi ram üzerinden kalıcı olarak siler.


# .remove() => dizinin elemanını siler(geriye None değerini teslim eder (geriye bişey teslim etmez :) ))
# .remove() => parametre olarak object(nesnenin bir örneğini) alır.

# .pop()    => dizinin elemanını siler(geriye silinen elemanı teslim eder.) 
# .pop()    => dizinin içerisinde silinecek olan elemanın index değerini alır. 


cities = ["ankara"]
del cities[0]
print(cities) # => []
