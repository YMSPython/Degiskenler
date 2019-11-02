# Ogrenci          : isim, soyisim, okul_numarası, TCKN,  sınıf, mail, telefon
# Ogretmen         : isim, soyisim,              , TCKN,  sınıf, mail, telefon, maas, gorev, brans
# Mudur Yardimcisi : isim, soyisim,              , TCKN,       , mail, telefon, maas, gorev
# Mudur            : isim, soyisim,              , TCKN,       , mail, telefon, maas, gorev
# Memur            : isim, soyisim,              , TCKN,       , mail, telefon, maas, gorev
# Hizmetli         : isim, soyisim,              , TCKN,       ,     , telefon, maas, gorev


class BaseClass():
    def __init__(self, isim="", soyisim="", TCKN="", telefon=""):
        self.isim = isim
        self.soyisim = soyisim
        self.TCKN = TCKN
        self.telefon = telefon

    def __str__(self):
        return "{} {} {} {}".format(self.isim, self.soyisim, self.TCKN, self.telefon)


class Personel(BaseClass):
    def __init__(self, isim="", soyisim="", TCKN="", telefon="", maas="", gorev=""):
        self.maas = maas
        self.gorev = gorev
        super().__init__(isim, soyisim, TCKN, telefon)
        #BaseClass.__init__(isim, soyisim, TCKN, telefon)

    def __str__(self):
        return "{} {} {}".format(super().__str__(), self.maas, self.gorev)


personel = Personel("murat", "vuranok", "12345678911",

                    "+905323520997",  10000000, "İşsiz")

print(personel)

class Ogrenci(BaseClass):
    okul_numarası = ""
    mail = ""
    sinif = ""


class Ogretmen (Personel):
    brans = ""
    sınıf = ""
    mail = ""


class MudurYardimcisi(Personel):
    mail = ""


class Mudur(Personel):
    mail = ""


class Memur(Personel):
    mail = ""


class Hizmetli(Personel):
    pass
