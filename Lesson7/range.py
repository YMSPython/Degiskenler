# range(başlangıç değeri, son değer, arttırma - azaltma)
toplam = 0
for i in range(1, 100):
    toplam += i

print(toplam)

toplam = 0
for i in range(100):  # 0,1,2,3,4,5,6...
    toplam += i
print(toplam)

toplam = 0
for i in range(1, 100, 2):  # 1,3,5,7,9...
    print(i)

for i in range(10, 0, -1):  # 10,9,8,7,6...
    print(i)

for i in range(10, 0, -2):  # 10,8,6,4,2
    print(i)

for i in range(2, 11, 2):  # 10,8,6,4,2,2,4,6,8,10
    print(i)

for i in range(-5, 5):  # -5, -4,-3,-2,-1,0,1,2,3,4,
    print(i)

#10'un katlaını yazdırma örneği
for i in range(16):
    print("{0:3} {1:16}".format(i,10**i))