from abc import ABCMeta, abstractmethod


class BasePhone(metaclass=ABCMeta):

    def __init__(self, marka, model, fiyat):
        self.Marka = marka
        self.Model = model
        self.Fiyat = fiyat

    @abstractmethod  # abstract olarak işaretlenmiş bir nesnenin, gövdesi olamaz. zorunlu olarak overide edileceğinden dolayı içerisindeki değere ulaşamazsınız
    def Sound(self):
        pass

    def __str__(self):
        return "Marka : {}\nModel : {}\nFiyat : {}\nTelefon Sesi : {}".format(self.Marka, self.Model, self.Fiyat, self.Sound())


class Samsung(BasePhone):
    def __init__(self, marka, model, fiyat, tedarikci):
        super(Samsung, self).__init__(marka, model, fiyat)
        self.Tedarikci = tedarikci

    def Sound(self):
        return "Samsung Telefon Sesi"


class Apple(BasePhone):
    def __init__(self, marka, model, fiyat, garanti):
        super(Apple, self).__init__(marka, model, fiyat)
        self.Garanti = garanti

    def __str__(self):
        return "{}\nGaranti Süresi : {}".format(super().__str__(), self.Garanti)

    def Sound(self):
        return "Apple Telefon Sesi"


class Nokia(BasePhone):
    def __init__(self, marka, model, fiyat, isletimSistemi):
        super(Nokia, self).__init__(marka, model, fiyat)
        self.IsletimSistemi = isletimSistemi

    def Sound(self):
        return "Nokia Telefon Sesi"


apple = Apple("IPhone", "X", 10000000000, 2)
print(apple)
