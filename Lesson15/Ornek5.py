from enum import Enum


class Color(Enum):
    Red = 1
    Green = 2
    Blue = 3


class Status(Enum):
    Active = 1
    Passive = 2
    Deleted = 5


print(Color.Blue)
print(repr(Color.Green))
print(type(Color.Red))

# birinci parametrede verilen değerin, ikinci parametenin bir değerimidir ?
print(isinstance(Color.Red, Color))

print(Color.Red.name)  # verdiğiniz enum değerinin adını teslim eder.


class Personel():
    def Delete(self, id):
        self.Status = Status.Deleted