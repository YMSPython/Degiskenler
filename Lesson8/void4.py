# 1 ile 1000 arasında yer alan sayıların toplamını ekrana yazdırınız(1 ve 1000 dahil)


def Toplama():
    result = 0
    for i in range(1, 1001):
        result += i
    print(result)
 
Toplama()
