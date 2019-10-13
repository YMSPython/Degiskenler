# kullanıcıdan şifre istenecek, eğer kullanıcı 3 defa yanlış şifre girerse, hesabınız bloke oldu, doğru girerse hoşgeldiniz. uyarısı verdiriniz.
for i in range(3):
    password = input("Lütfen şifrenizi giriniz : ")

    if not password:
        print("Şifre alanı boş geçilemez")
        

    if password == "Password1": # parola doğru girilirse
        print("Hoşgeldiniz :)")
        break # koşul sağlandığı için, işlemi sonlandırıyoruz.
    else:
        if i == 2:  # şifre 3 defa yanlış girildi
            print("şifrenizi 3 defa yanlış girmeyi başardınız. tebrikler :)")
            break
              
        if len(password) in range(3, 8):# password 3 ile 8 karakter aralığında olmalıdır.
            print("Karakter sayısı yeterli olsada, şifre yine yanlış :)")
        else:
            print("Parolanız 3 ile 8 karakter aralığında olmalıdır.")

