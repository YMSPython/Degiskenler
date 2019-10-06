# Örnek :  Dışarıdan girilen ürün adına göre, kullanıcıya o ürünün hangi reyonda yer aldığını söyleyen uygulama yazınız.


# Domates, Biber, Patlıcan => Manav Reyonu
# Diş Macunu, Parfüm, Şampuan => Kozmetik Reyonu
# Cep Telefonu, Bilgisayar, Tablet => Teknoloji Reyonu

_urun = input("Lütfen ürün adını giriniz : ").lower().replace('ç','c')
_bildirim = "Aradığınız Ürün {} Reyonunda Yer Almaktadır!" 

if _urun == "domates" or _urun == "biber" or _urun == "patlıcan":
    print(_bildirim.format("Manav"))
elif _urun == "diş macunu" or _urun == "parfüm" or _urun == "şampuan":
    print(_bildirim.format("Kozmetik"))
elif _urun == "cep telefonu" or _urun == "bilgisayar" or _urun == "tablet":
    print(_bildirim.format("Teknoloji"))
else:
    print("Bizde Böyle Bir Ürün Yoktur!")