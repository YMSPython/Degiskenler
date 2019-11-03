from abc import ABCMeta, abstractmethod


class BaseClass (metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    @abstractmethod
    def printMetot(self):
        return "base dosya"


class Personel(BaseClass):

    def printMetot(self):
        return "Personel dosyası yazdırıldı"


class Ogrenci(BaseClass):
    def printMetot(self):
        return "Öğrenci dosyası yazdırıldı"


per = Personel()
print(per.printMetot())

ogr = Ogrenci()
print(ogr.printMetot())


# Giyim, Gıda, Ziynet, Teknoloj, Otomotiv

class BClss(metaclass=ABCMeta):
    #__metaclass__ = ABCMeta
    @abstractmethod
    def KDV(self):
        return 0


class Giyim (BClss):
    def KDV(self):
        return 18

print(Giyim().KDV())
