class Personel:
    isim = ""
    soyisim = ""
    telefon = ""
    mail = ""

    def __init__(self, firstname="", lastname="", phone="", mail=""):  # constructor (yapıcı metot)
        self.isim = firstname
        self.soyisim = lastname
        self.mail = mail
        self.telefon = phone

    def __str__(self):
        return "Personel Adı : {0}\nPersonel Soyadı : {1}\nPersonel Telefon : {2}\nPersonel Mail : {3}".format(self.isim, self.soyisim, self.telefon, self.mail)


# emp = Personel()
# emp.isim = "Murat"
# emp.soyisim = "Vuranok"
# emp.telefon = "+905323529999"
# emp.mail = "murat.vuranok@bilgeadam.com"


# print(emp)


per1 = Personel("murat", "vuranok", "+905323529999",
                "murat.vuranok@bilgeadam.com")
print(per1)

per2 = Personel("ahmet", "vuranok", "+905323529999",
                "murat.vuranok@bilgeadam.com")
print(per2)


per3 = Personel()
per3.isim = "Koray"
print(per3)
