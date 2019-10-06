# karar yapıları  if - elif - else
# karşılaştırma operatorleri

# == (Eşittir) Soldaki değerin, sağdaki değere eşit olma durumu

result = (1 == 2)  # => False teslim eder.
result = (1 == 1)  # => True teslim eder.
print(result)

# != (Eşit Değildir) Soldaki değerin, sağdaki değere eşit olmama durumu
result = (1 != 2)  # True teslim eder
print(result)
result = (1 != 1)
print(result)

# > (Büyüktür) => soldaki değerin, sağdaki değerden büyük olma durumu
result = (20 > 10)  # True
print(result)
result = (10 > 20)  # False

# < (Küçüktür) => soldaki değerin, sağdaki değerden küçük olma durumu

result = (10 < 20)  # True
print(result)
result = (20 < 10)  # False
print(result)


# >= (Büyük veya Eşit) => soldaki değerin, sağdaki değerden büyük veya eşit olma durumu

result = (10 >= 7)  # True (büyük olma durumu)
result = (10 >= 10)  # True (eşit olma durumu)
result = (1 >= 2)   # False (koşullar sağlanamadı)

# <= (Küçük veya Eşit) => soldaki değerin, sağdaki değerden küçük veya eşit olma durumu
result = (1 <= 2)  # True (küçük olma durumu)
result = (1 <= 1)  # True (eşit olma durumu)
result = (2 <= 1)  # False (koşullar sağlanamadı)


username = "admin"  # database'den gelen kullanıcımız.
kullaniciAdi = input("Lütfen Kullanıcı Adınızı Giriniz :")
print(kullaniciAdi.lower())


kullaniciAdi = kullaniciAdi\
.replace('İ','I')\
.lower()\
.replace('ı','i')\
.replace('ç','c')\
.replace('ş','s')\
.replace('ğ','g')\
.replace('ö','o')\
.replace('ü','u')\
.replace(' ','')

  
if kullaniciAdi == username:
    print("Hoşgeldiniz!")
else:
    print("Kullanıcı Adınız Yanlış!")
 
# hepsini küçük harfe çevirip, türkçe karakterler temizleyiniz :)
# replace ve lower metotları

print(ord('i̇'))
 