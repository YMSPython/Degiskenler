from random import randint


numbers = []
while True:
    i  = 0
    sayilar = []
    while i < 6:
        sayi = randint(1,49)
        if sayilar.count(sayi):
            i -= 1
        else:
            sayilar.append(sayi) 
        i+= 1
    sayilar.sort()
    numbers.append(sayilar)
    if len(numbers) == 8:
        break
  
print(numbers)

 
 # [3,  5,  10, 14, 41, 49], 
 # [13, 21, 26, 33, 36, 40], 
 # [1,  19, 22, 28, 41, 42], 
 # [7,  18, 25, 33, 45, 48], 
 # [1,  5,  27, 28, 41, 48], 
 # [3,  4,  12, 16, 28, 29], 
 # [7,  11, 33, 34, 37, 39], 
 # [1,  11, 13, 16, 20, 22] 