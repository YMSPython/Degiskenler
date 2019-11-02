class Calisan():

    def __init__(self, isim, soyisim, maas, departman, yas=10):
        print("Çalışan sınıfının yapıcı metodu çalıştı")
        # constructor
        self.FirstName = isim
        self.LastName = soyisim
        self.Salary = maas
        self.Department = departman
        self.Age = yas

    def __str__(self):
        return "Personel Adı : {}\nPersonel Soyadı : {}".format(self.FirstName, self.LastName)

    def Info(self):
        print("Personel Adı : {}\nPersonel Soyadı : {}\nPersonel Departmanı : {}\nPersonel Yaşı : {}\nPersonel Maaşı : {}".format(
            self.FirstName, self.LastName, self.Department, self.Age, self.Salary))

    def SalaryRaise(self, raiseRate):
        print("Çalışanın Maaş Bilgisi Güncellendi!")
        _salary = self.Salary
        self.Salary += raiseRate
        print("{} adlı personelin maaşı {}'(dan-den) {}'(a-e) yükseltilmiştir! ".format(
            (self.FirstName + " " + self.LastName), _salary, self.Salary))

    def ChangeDepartment(self, newDepartment):
        print("Personelin Departmanı Değiştirildi!")
        _department = self.Department
        self.Department = newDepartment
        print("{} adlı personelin departmanı {}'(dan-den) {}'(a-e) departmanı olarak güncellenmiştir! ".format(
            (self.FirstName + " " + self.LastName), _department, self.Department))


personel = Calisan('murat', 'vuranok', 1000000, 'yazılım', 38)
print(personel)
personel.Info()
personel.SalaryRaise(1000000)
personel.ChangeDepartment("Yönetim Kurulu")


# C#    inheritance =>  A : B
# Java  inheritance =>  A extend B
# React inheritance =>  A extend B
# Pyton inheritance =>  A(B)

class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, departman, personelSayisi, yas=10):
        print("Yönetici sınıfı, yapıcı metodu çalıştı")
        self.FirstName = isim
        self.LastName = soyisim
        self.Salary = maas
        self.Department = departman
        self.Age = yas
        self.NumberOfEmployee = int(personelSayisi)

    def print_base(self):
        for base in self.__class__.__bases__:
            print("Miras Aldığı Sınıf :", base.__name__)

    def __str__(self):
        return "{} {} {}".format(self.FirstName, self.LastName, self.Department)


yonetici = Yonetici("murat", "vuranok", 100000000, "yazılım", 1, 38)
print(yonetici)
yonetici.Info()
yonetici.print_base()
