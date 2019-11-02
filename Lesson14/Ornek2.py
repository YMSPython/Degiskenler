class ParentClass():
    def send_message(self):
        print('Bu alan içerisinde mesaj vereceğiz')


class Baseclass(ParentClass):
    def send_message(self):
        print("Bu alan içerisinde de mesaj vereceğiz")


parent = ParentClass()
parent.send_message()

base = Baseclass()
base.send_message()