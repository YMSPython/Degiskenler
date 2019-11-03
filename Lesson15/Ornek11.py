from enum import Enum


class RenkEnum(Enum):
    Kırmızı = 1
    Sarı = 2
    Mavi = 'Blue'
    Mail = "Mail Adresi @ işareti içermelidir. Lütfen kontrol ediniz"


print(repr(RenkEnum.Mavi))
print(repr(RenkEnum.Mail.value))


class IntEnum(int, Enum):
    Kırmızı = 1
    Sarı = 2
    #Mavi = "blue"


print(IntEnum.Kırmızı)
