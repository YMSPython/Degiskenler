from datetime import datetime
from datetime import timedelta

class Personel:
    FirstName = ""
    LastName  = ""
    Mail      = ""
    Phone     = ""
    Address   = ""
    FireDays  = "" 
    HireDate  = "{}/{}/{} {}:{}".format(
        datetime.now().day,
        datetime.now().month, 
        datetime.now().year,
        datetime.now().hour,
        datetime.now().minute)

    def IseAl(self):
        print("""
        Personel Adı                   : {}
        Personel Soyadı                : {}
        Personel Telefon               : {}
        Personel Mail                  : {}
        Personel Adres                 : {}
        Personel İşe Giriş Tarihi      : {}
        Personel Sözleşme Bitiş Tarihi : {}

        Personelin İşe Girişi Tamamlandı!
        """.format( 
            self.FirstName, 
            self.LastName, 
            self.Phone, 
            self.Mail, 
            self.Address,
            self.HireDate, 
            "{}/{}/{} {}:{}".format(
                (datetime.now() + timedelta(days = self.FireDays)).day,
                (datetime.now() + timedelta(days = self.FireDays)).month,
                (datetime.now() + timedelta(days = self.FireDays)).year,
                (datetime.now() + timedelta(days = self.FireDays)).hour,
                (datetime.now() + timedelta(days = self.FireDays)).minute
            )))


calisan = Personel()
calisan.FirstName = "Murat"
calisan.LastName  = "Vuranok"
calisan.Mail      = "murat.vuranok@bilgeadam.com"
calisan.Phone     = "+905325678990"
calisan.Address   = "Bilge Adam/Beşiktaş"
calisan.FireDays  = 150
print(calisan.IseAl())

