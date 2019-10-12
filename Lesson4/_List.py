# Tanımlama şekli
sehirler = ["Adana", "Ankara", "Antalya", "Edirne", "Malatya", "Maraş"]
# print("\n".join(sehirler))


index = len(sehirler) - 1
# print(sehirler[index])

# 1. parametrede verilen değer başlangıç index değeridir. 2. parametrede verilen index değerinin 1 alt değerine kadar olan elemanlar listelenecektir.
# print(sehirler[2:5])

# print('Adana' in sehirler)  # sehirler dizisi içersinde 'Adana' ili var ise True değerini teslim eder.

# print('Adana' not in sehirler)  # sehirler dizisi içersinde 'Adana' ili yok ise, True değerini teslim eder.

result = 'Adana' in sehirler
# Ternary Operatoru
print("Adana dizi içerisinde geçmektedir" if result else "Adana Dizi içerisinde Geçmemektedir")

# Console.WriteLine(result ? "Adana dizi içerisinde geçmektedir" : "Adana Dizi içerisinde Geçmemektedir") => C#


x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
a = list(zip(x,y,z))
print(a[0][:]) 