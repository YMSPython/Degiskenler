_not = int(input("Lütfen notunuzu giriniz : "))
_bildirim = "Harf Notunuz : {}"

# if not(_not < 0) and not(_not > 100):
if _not >= 0 and _not <= 100:
    if _not <= 30:
        _bildirim = _bildirim.format("FF")
    elif _not <= 50:
        _bildirim = _bildirim.format("DD")
    elif _not <= 70:
        _bildirim = _bildirim.format("CC")
    elif _not <= 85:
        _bildirim = _bildirim.format("BB")
    else:
        _bildirim = _bildirim.format("AA")
else:
    _bildirim = _bildirim.format("Geçerisiz!!")
print(_bildirim)
