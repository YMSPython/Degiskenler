# Dışarıdan girilen sayıların birbiriyle olan toplam değerini ekrana yazdırınız.

# 123 = 6

gelen = input("Lütfen sayı giriniz : ")
i = 0
result = 0
while i < len(gelen):
    result += int(gelen[i])
    i += 1  
print(result)