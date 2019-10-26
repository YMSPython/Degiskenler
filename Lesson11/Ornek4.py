# split() => elindizdeki değeri verdiğiniz karakterden ayırarak size dizi teslim eder

elemanlar = "yazılım,sistem,grafik,teknik çizim,muhasebe"
print(elemanlar)

# yazılım,
# sistem,
# grafik,
# teknik çizim,
# muhasebe

# parametre vermeden ayırma işlemi yaparsanız, default olarak boşluklardan ayırma işlemi yapar
print(elemanlar.split())

# ['yazılım,sistem,grafik,teknik', 'çizim,muhasebe']

print(elemanlar.split(','))
# ['yazılım', 'sistem', 'grafik', 'teknik çizim', 'muhasebe']

print(elemanlar.split(',', 3))
['yazılım', 'sistem', 'grafik', 'teknik çizim,muhasebe']