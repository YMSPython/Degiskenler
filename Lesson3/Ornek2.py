  
# Örnek : Girilen not değeri 0’dan küçük ise, 0’dan küçük not giremezsiniz. 100’den büyük bir değer girerseniz 100’den büyük not girişi yapamazsınız uyarı verdiren uygulama yazınız.


try:
    not_ = int(input("Lütfen notunuzu giriniz : "))
    if not_ < 0 :
        print("0'dan küçük not girişi yapamazsınız!")
    elif not_ > 100:
        print("100'den büyük not girişi yapamazsınız!")
    else:
        print("Notunuz :", not_)
except Exception as ex:
    print(ex)
    

