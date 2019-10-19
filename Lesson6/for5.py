# dışarıdan aldığı değere göre içi dolu kare çiziniz..
kare = int(input("Lütfen bir değer gir10iniz : "))

for index  in range(kare): 
    deger = ""
    for i in range(kare):
        deger += "X "
    print(deger)

print("-" * 50)
i = 0 # 1
while i < kare: # 10
    print("X " * kare) ############
    i += 1 