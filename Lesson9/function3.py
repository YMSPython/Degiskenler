# Disaridan girilen ilk kelimenin ilk iki harfini buyuk,
# geri kalanini kucuk aliniz..
# ikinci kelimenin icerisinde gecen tum a'lari e'ile degistiriniz
# ve sonuna @hotmail.com ekleyerek geri dondurunuz...

# murat
# MUrat


def MailAdresiCreate(isim, soyisim):
    _isim = "{}{}".format(isim[0:2].upper(), isim[2:].lower())
    _soyisim = soyisim.replace("a", "e").lower()
    return "{}.{}@hotmail.com".format(_isim, _soyisim)


mail = MailAdresiCreate(input("Lütfen Adınızı Giriniz : "),
                        input("Lütfen Soyadınızı Giriniz : "))
print(mail)
# MUrat.vurenok@hotmail.com

