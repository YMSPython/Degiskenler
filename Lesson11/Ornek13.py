# .index()
# .rindex()


metin = "murat.vuranok@bilgeadam.com@bilge"
# isim       = murat
# soyisim    = vuranok
# mail       = murat.vuranok@bilgeadam.com
# firma      = bilgeadam
# web sitesi = bilgeadam.com



print(metin[0:metin.index('@')])
print(metin.index('@')) # => metin içerisinde parametredeki ilk buluğu yerdeki index'i teslim eder
print(metin.rindex('@')) # => metin içerisinde parametredeki en son geçtiği yerin index değerini teslim eder.


metin = "bilgeadam"
print(metin.index('@'))