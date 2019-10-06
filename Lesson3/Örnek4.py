# Mantıksal operatoler

# and  sorguya katılan her bir koşulun sağlanması durumu
# or   sorguya katılan hergangi bir koşulun sağlanması durumu
# not  sorguya olumsuzluk katar True ise False, False ise True


username = input("Kullanıcı Adınızı Giriniz : ")
 
if username == "admin":
    password = input("Şifrenizi Giriniz : ")
    if password == "123":
        print("Tebrikler!")
    else:
        print("Şifreniz Hatalı!")
else:
    print("Kullanıcı Adınız Yanlış")


