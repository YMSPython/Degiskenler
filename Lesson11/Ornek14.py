# .find()  
# .rfind()
 


metin = "murat.vuranok@bilgeadam.com@bilge"
# isim       = murat
# soyisim    = vuranok
# mail       = murat.vuranok@bilgeadam.com
# firma      = bilgeadam
# web sitesi = bilgeadam.com



print(metin[0:metin.find('@')])
print(metin.find('@')) # => metin içerisinde parametredeki ilk buluğu yerdeki index'i teslim eder
print(metin.rfind('@')) # => metin içerisinde parametredeki en son geçtiği yerin index değerini teslim eder.


metin = "bilgeadam"
print(metin.find('@'))