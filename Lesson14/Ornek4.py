class Cup1():
    def __init__(self):
        self.color = None  # public variable
        self.content = None  # public variable

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def __str__(self):
        return self.color + " " + self.content


cup1 = Cup1()
cup1.color = "Red"
cup1.content = "tea"
print(cup1)

cup1.empty()
cup1.color = 'black'
cup1.content = 'coffee'
print(cup1)


class Cup2():
    def __init__(self):
        self.color = None   # public variable(property)
        self._content = None  # protected(korumalı)
        # korulamı üye, c# gibi dillerde miras alınan sınıflarda görünsede, python dilinde tek bir çizgi(_) var ise, bana dokunma anlamına gelir :)

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

    def __str__(self):
        return self.color + " " + self._content


cup2 = Cup2()

cup2.color = "Red"
cup2._content = "tea"

print(cup2)


class Cup3():
    def __init__(self, color):
        self._color = color   # public variable(property)
        # private, eğer __ iki adet çizgiden oluşuyorsa private değişken anlamına gelir.
        self.__content = None

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def __str__(self):
        return self._color + " " + self.__content


cup3 = Cup3("blue")

#cup3._color = "Kırmızı"
#cup3.__content = "Çay"

cup3._Cup3__content = "Çay"

print(cup3)
