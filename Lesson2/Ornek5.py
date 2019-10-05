try:
    sayi = int(input("sayı giriniz"))
except Exception as ex:
    print(ex)
finally:
    print("her durumda çalışırımm")