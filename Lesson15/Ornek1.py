import datetime

now = datetime.datetime.now()

print(str(now))
print(now)
print(repr(now))


class Personel():
    def __init__(self, firstname):
        self.FirstName = firstname

    def __repr__(self):
        return "Personel('{}',{})".format(self.FirstName, self.FirstName)

    def __str__(self):
        return '{}-{}'.format(self.FirstName, self.FirstName)

per = Personel("Murat")
print(str(per))
print(per) 
print(str(repr(per))) # Personel('Murat',Murat)

print(per.__repr__()) # developer için devam niteliğinde kod teslim eder.
print(per.__str__())  # son kullanıcı için çıktı verir.