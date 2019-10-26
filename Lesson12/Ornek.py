# kullanıcıdan şirken maili ve telefon numarasını alınız. ve çıktı olarak ekrana aşağıda yer alan formata göre yazdırınız.

# murat.vuranok@bilgeadam.com
# 5323520997
# 05323520997
#
# İsim    : Murat
# Soyisim : Vuranok
# Telefon : +(90)532 352 0997
# Mail    : murat.vuranok@bilgeadam.com

mail = input("Lütfen mail adresinizi giriniz : ")
isim = mail[0:mail.index('.')]
soyisim = mail[mail.index('.') + 1: mail.index('@')] 
telefon = input("Lütfen telefon numaranızı giriniz : ")

while True: 
    if(telefon.startswith('0') and len(telefon) == 11):
        telefon = "+9{0} ({1}) {2} {3}".format(
            telefon[0:1], telefon[1:4], telefon[4:7], telefon[-4:])
        break
    elif(not telefon.startswith("0") and len(telefon) == 10):
        telefon = "+90 ({0}) {1} {2}".format(
            telefon[0:3], telefon[3:6], telefon[-4:])
        break
    else:  
        telefon = input(
            "Lütfen telefon numaranızı giriniz, Telefon numarsı formatını görmek istiyorsanız, lütfen (f) tuşuna basınız : ")
        if(telefon == "f" or telefon == "F"):
            print("Geçerli Telefon Formatları : 5323456677 - 05323456677")
            continue


print("""
İsim           : {0}
Soyisim        : {1}
Telefon        : {2}
Mail Adresiniz : {3}
""".format(isim, soyisim, telefon, mail))
