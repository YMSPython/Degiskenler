# 1 ile 1000 arasında yer alan, tek ve çift sayıların adedini ekrana yazdırınız.

i = 1
teksayilar = 0
ciftsayilar = 0
while i <= 1000:
    if i % 2 == 0:
        ciftsayilar += 1
    else:
        teksayilar += 1
    i += 1
print("çift sayıların toplamı : {}\ntek sayıların toplamı : {}".format(ciftsayilar,teksayilar))