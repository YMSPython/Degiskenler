# Örnek :  //Disaridan siparis alinacak olan kitap miktari girilsin. Sipari sayisi 20'den azsa toplam ucretten %5, 20 - 50 araliginda ise %10, 50-100 araligi ise %15, 100'den fazla ise %25 indirim yapilsin. Kitabın birim fiyatı => 5 TLdir... Amac => Odenecek tutari kullaniciya gostermek...

try:
    birimFiyat = 5
    siparisMiktari = int(input("Lütfen sipariş adedi giriniz : "))
    toplamTutar = 0
    mesaj = "Toplamda Ödemeniz Gereken Tutar :"
    if(siparisMiktari > 0):
        if siparisMiktari <= 20:
            toplamTutar = (birimFiyat * siparisMiktari) * 0.95
        elif siparisMiktari >  20 and siparisMiktari <= 50:
            toplamTutar = (birimFiyat * siparisMiktari) * 0.90
        elif siparisMiktari > 50  and siparisMiktari < 100:
            toplamTutar = (birimFiyat * siparisMiktari) * 0.85
        elif siparisMiktari > 100:
            toplamTutar = (birimFiyat * siparisMiktari) * 0.75 
        mesaj += str(toplamTutar)
        print(mesaj)
    else:
        print("Lütfen 0'dan büyük bir değer giriniz!")
except Exception as ex:
    print(ex)