#1000 ile 1 arasındaki sayıları yazdırınız.
def Saydir():
    i = 1000
    while i >= 1:
        print(i)
        i -= 1

Saydir()

def SaydirVol2():
    for i in range(1000, 0, -1):
        print(i)

SaydirVol2()