# .strip()  => (trim)  metnin başındaki ve sonundaki boşlukları temizler
# .lstrip() => soldaki boşlukları siler
# .rstrip() => sağdaki boşlukları siler

metin = "      bilge adam      "
print(len(metin))
print(metin)
metin = metin.strip()
print(len(metin))
print(metin)