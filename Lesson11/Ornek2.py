# sorted() => dizi içerisinde yer alan elemanları A'dan Z'ye, 0'dan 9'a sıralam yapar.

import locale
deger = sorted('bilge adam')
print(deger)
# [' ', 'a', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'm']

# Türkçe karakterleri dizinin en sonuna atar.

deger = sorted("üğişççöbilge adam")
print(deger)
# [' ', 'a', 'a', 'b', 'd', 'e', 'g', 'i', 'i', 'l', 'm', 'ç', 'ç', 'ö', 'ü', 'ğ', 'ş']

# alfabetik sıraya göre değil Ascii kod üzerinden devam eder. düzeltmek için.

locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")  # windows için
# locale.setlocale(locale.LC_ALL,"tr_TR") # Linux

deger = sorted("üğişççöbilge adam", key=locale.strxfrm)
print(deger)

#[' ', 'a', 'a', 'b', 'd', 'e', 'g', 'i', 'i', 'l', 'm', 'ç', 'ç', 'ö', 'ü', 'ğ', 'ş']
#[' ', 'a', 'a', 'b', 'ç', 'ç', 'd', 'e', 'g', 'ğ', 'i', 'i', 'l', 'm', 'ö', 'ş', 'ü']
