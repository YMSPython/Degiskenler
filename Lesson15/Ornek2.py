class Personel:
    def __init__(self, isim="", soyisim=""):
        self.FirstName = isim
        self.LastName = soyisim

    @property  # Get Metodu (Sadece okunabilir) getter
    def Mail(self):
        return "{}.{}@bilgeadam.com".format(self.FirstName.lower(), self.LastName.lower())

    @property
    def isim_soyisim(self):
        return "{} {}".format(self.FirstName, self.LastName)

    @isim_soyisim.setter
    def isim_soyisim(self, parameters):  # 'murat vuranok'
        ad, soyad = parameters.split(' ')
        self.FirstName = ad
        self.LastName = soyad

    @isim_soyisim.deleter
    def isim_soyisim(self):
        print("Kişi silindi")
        self.FirstName = None
        self.LastName = None


personel = Personel("Murat", "Vuranok")
print(personel.FirstName)
print(personel.LastName)
print(personel.Mail)

personel.isim_soyisim = "Ahmet Şahin"
print(personel.FirstName)
print(personel.LastName)
print(personel.Mail)


print(personel.isim_soyisim)
del personel.isim_soyisim

pe = Personel(soyisim="", isim="Murat")
