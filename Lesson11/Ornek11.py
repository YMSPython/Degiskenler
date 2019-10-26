# .join() => dizi içerisindeki elemanları birleştirmek için kullanılır
metin = "yazılım,sistem,grafik,muhasebe,ofis,teknik çizim,mobil,oyun".replace(" ","")
result = metin.split(',')

print("-".join(result))