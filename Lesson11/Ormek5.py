# rsplit() içerisinde verilen parametrekeri (,.;) sağdan sola doğru ayırma işlemi yapar

elemanlar = "yazılım,sistem,grafik,teknik çizim,muhasebe"
print(elemanlar.split(',',3))
print(elemanlar.rsplit(',',3))

# ['yazılım', 'sistem', 'grafik', 'teknik çizim', 'muhasebe']

#['yazılım', 'sistem', 'grafik', 'teknik çizim,muhasebe']
#['yazılım,sistem', 'grafik', 'teknik çizim', 'muhasebe']
