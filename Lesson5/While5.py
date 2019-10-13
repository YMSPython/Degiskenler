# Kullanıcı dışarıdan bir metin girecek, ve girilen metnin her bir karakterini,alt alta yazdırınız
#bilge adam
metin = input("Lütfen bir metin giriniz! : ")
i = 0
key = ""
while(i < len(metin)):
    key+=metin[i]+"\n"
    print(metin[i])
    i+=1
print(key)

# string aslında bir char(karakter) dizisidir