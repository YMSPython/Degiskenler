username = input("Kullanıcı Adınızı Giriniz : ")
password = input("Şifrenizi Giriniz : ")

if (username == "admin" or username == "admin@admin.com") and (password == "123" or password == "1234"):
    print("Giriş yaptınız!")
else:
    print("Kullanıcı bilgilerinizi kontrol ediniz!")

if(username == "{}.{}".format("murat","vuranok")):
    username = "{}.{}@bilgeadam.com".format("murat","vuranok")

# murat.vuranok
# murat.vuranok@bilgeadam.com

