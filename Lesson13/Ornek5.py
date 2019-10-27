# __str__ C# .ToString()


class Personel:
    FirstName = ""
    LastName = ""
    Mail = ""
    Phone = ""

    def __str__(self):
        # return <__main__.Personel object at 0x1006873c8>
        return "{} {}".format(self.FirstName, self.LastName)


personeller = []
# personel1 = Personel()
# personel1.FirstName = "Murat"
# personel1.LastName = "Vuranok"
# personel1.Phone = "+905434323425"
# personel1.Mail = "murat.vuranok@bilgeadam.com"


# personel2 = Personel()
# personel2.FirstName = "Ahmet"
# personel2.LastName = "Mehmet"
# personel2.Phone = "+905434323425"
# personel2.Mail = "ahmet.mehmet@bilgeadam.com"

# print(personel1)
# print(personel2)


while True:
    print("Personel Ekleme Ekranına Hoşgeldiniz")
    print("Personel Ekleme İşlemi İçin (a)")
    print("Personel Listesi İçin (l)")
    go_on = input("Lütfen bir anahtar kelime giriniz : ").lower()
    if go_on == 'a':
        firstname = input("Personel Adını Giriniz : ")
        lastname = input("Personel Soyadını Giriniz : ")
        phone = input("Personel Telefon Numarasını Giriniz : ")
        mail = input("Personel Mail Adresini Giriniz : ")

        personel = Personel()
        personel.FirstName = firstname
        personel.LastName = lastname
        personel.Mail = mail
        personel.Phone = phone

        personeller.append(personel)
    elif go_on == 'l':
        for p in personeller:
            print(p)
