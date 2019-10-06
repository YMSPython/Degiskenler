# Örnek : Dışarıdan girilen not aralığı
#  0 – 30  =>  FF
# 31 – 50  =>  DD
# 51 – 70  =>  CC
# 71 – 85  =>  BB
# 86 – 100 =>  AA ,  harf notunu aldınız uyarısını kullanıcıya veriniz.


_not = int(input("Lütfen notunuzu giriniz : "))
_bildirim = "Harf Notunuz : {}"
if _not >= 0 and _not <= 30:
    _bildirim = _bildirim.format("FF")
elif _not >= 31 and _not <= 50:
    _bildirim = _bildirim.format("DD")
elif _not >= 51 and _not <= 70:
    _bildirim = _bildirim.format("CC")
elif _not >= 71 and _not <= 85:
    _bildirim = _bildirim.format("BB")
elif _not >= 86 and _not <= 100:
    _bildirim = _bildirim.format("AA")
else:
    _bildirim = _bildirim.format("Geçersiz!")
print(_bildirim)
