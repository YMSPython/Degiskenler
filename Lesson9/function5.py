# Kullanıcı dışarıdan dilediği kadar sayı girecek, her sayı girdikten sonra, sayı girmeye devam edip etmeyeceği sorulacak. :)

# kullanıcı y Y tuşuna basarsa, yeni bir sayı girmesi istenilecek
# kullanıcı harici bir tuşa basar ise, içeriye aldığı sayılar içerindeki tek sayılar içerisinde yer alan en büyü ve en küçün sayının biribirine olan farkını geriye dönecek :)


# https://www.packtpub.com/free-learning

 
def FarkiHesapla():
    go_on = 'y'
    tek_sayilar = []
    while go_on == 'y' or go_on == 'Y':
        number = float(input("Lütfen bir sayı giriniz : "))
        if number % 2 != 0: #sayı tektir.
            tek_sayilar.append(number)
        go_on = input("Yeni bir sayı eklemek istiyormusunuz! (Y\\N) : ")

        if not go_on:
            while len(go_on) == 0:
                go_on = input("Yeni bir sayı eklemek istiyormusunuz! (Y\\N) : ")
    
    # tek_sayilar.sort()
    # _min = tek_sayilar[len(tek_sayilar) - 1]
    # _max = tek_sayilar[0]
    # _result = _max - _min
    
    return max(tek_sayilar) - min(tek_sayilar)



sonuc = FarkiHesapla()
print(sonuc)