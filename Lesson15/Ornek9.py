from enum import Enum, unique, auto


class Durum(Enum):
    Mutlu = 1
    Uzgun = 3

    def descripe(self):
        return self.name, self.value

    def __str__(self):
        return "Şuanki ruh halim dıgıdık dıgıdık gidiyor ama {} ".format(self.name)

    @classmethod
    def favori_durum(cls):
        return cls.Uzgun


print(Durum.favori_durum())
print(Durum.Uzgun.descripe())
print(str(Durum.Mutlu))