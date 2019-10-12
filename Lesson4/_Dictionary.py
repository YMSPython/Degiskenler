# Dictionary key value formatında dataları listelemek için kullanılır. Json formatında data tutar, MongoDb, WebApi (servisler), JavaScript (vue js, angular js, angular io, react, react-native, cordova vs) gibi  bir çok platform bunu destekler.

personeller = [
    {
        "Id": 1,
        "FirstName": "Murat",
        "LastName": "Vuranok",
        "Phone": 5323348899,
        "Mail": "murat.vuranok@bilgeadam.com"
    },
    {
        "Id": 2,
        "FirstName": "Ahmet",
        "LastName": "Şahin",
        "Phone": 5437778876,
        "Mail": "ahmet.sahin@bilgeadam.com"
    },
    {
        "Id": 3,
        "FirstName": "Mehmet",
        "LastName": "Budak",
        "Phone": 5323348899,
        "Mail": "mehmet.budak@bilgeadam.com"
    },
    {
        "Id": 3,
        "FirstName": "Sait",
        "LastName": "Şahin",
        "Phone": 5437778876,
        "Mail": "sait.sahin@bilgeadam.com"
    }
]

# print(personeller[0])  => dizinin ilk elemanını ekrana yazdırır
# print(personeller[1])  => dizinin ikinci elemanını ekrana yazdırır.

# print(personeller[:])  => dizi içerisinde yer alan tüm elemanları ekrana yazdırır.
# print(personeller[2:]) => verdiğiniz index numarası dahil dizinin geriye kalan elemanlarını ekrana yazdırır.
# print(personeller[2:3])


# print(personeller[0]["FirstName"])


# liste içerisinde yer alan herhangi bir data üzerinde değişiklik yapmak istiyorsak;
guncelleneceIndex = 1
guncelleneceKey = "FirstName"


eskiAdi = personeller[guncelleneceIndex][guncelleneceKey]
personeller[guncelleneceIndex][guncelleneceKey] = "Okan"
personeller[2]["FirstName"] = "Hasan"
personeller[2]["LastName"] = "Akın"

#print(eskiAdi)
#print(eskiAdi, "Adlı Personelin Yeni Adı :",
#personeller[guncelleneceIndex][guncelleneceKey], "Olarak Güncellenmiştir")


# dizi içerisine yeni bir eleman eklemek için;
yeniPersonel = {
    "Id":  6,
    "FirstName": "Ayşe",
    "LastName": "Akın",
    "Phone": "5431239989",
    "Mail": "ayse.akin@bilgeadam.com"
}
#personeller.append(yeniPersonel)
#print(personeller[len(personeller) -1])

print("Personel Adı : {}\nPersonel Soyadı : {}\nPersonel Telefon : {}\nPersonel Mail : {}".format(personeller[0]["FirstName"],personeller[0]["LastName"],personeller[0]["Phone"],personeller[0]["Mail"]))


