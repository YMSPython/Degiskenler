// show dbs           => server içerisinde yer alan db'leri listeler
// use TelefonRehberi => yeni bir database oluşturur
// show collections   => database içerisinde yer alan, tabloları listeler

// db.Kisiler.insert() => database içerisinde, verdiğiniz isimde bir tablo yok ise, tablo oluşturur ve içerisine kaydı ekler, eğer tablo var ise, kaydı ekler.

// Not : Tablo ve db ismine dikkat edin küçük büyük harf duyarlılığı vardır. İkinci bir db veya tablo oluşturabilirsiniz...

// FirstName  : Ad
// LastName   : Soyad
// Phone      : Telefon
// Mail       : EPosta
// Adress     : Adres

[
    {
        "Ad": "Murat",
        "Soyad": "Vuranok",
        "Telefon": "+905333533333",
        "EPosta": "murat.vuranok@bilgeadam.com"
    }
]

// db içerisine insert işlemi yapar (tek bir kayıt ekler)
db.Kisiler.insert({
    "Ad": "Murat",
    "Soyad": "Vuranok",
    "Telefon": "+905333533333",
    "EPosta": "murat.vuranok@bilgeadam.com"
})


db.Kisiler.insert({
    "Ad": "Mehmet",
    "Soyad": "Şahin",
    "Telefon": "+905333533333",
    "EPosta": "mehmet.sahin@bilgeadam.com",
    "Adres": "BilgeAdam\Beşiktaş"
})

db.Kisiler.insert({
    "_id": 1,
    "Ad": "Arif",
    "Soyad": "Susam",
    "Telefon": "+905333533333",
    "EPosta": "arif.susam@bilgeadam.com",
    "Adres": "BilgeAdam\Susam Sokağı"
})
// db.<tabloAdi>.find() => tablo içerisinde yer alan kayıtları listeler.
// db.<tabloAdi>.find().pretty() => tablo içerisinde yer alan kayıtları, formatlı bir şekilde listeler.


/*

{
        "_id" : ObjectId("5dc6cc19744d1094ab100a96"),
        "Ad" : "Murat",
        "Soyad" : "Vuranok",
        "Telefon" : "+905333533333",
        "EPosta" : "murat.vuranok@bilgeadam.com"
}
{
        "_id" : ObjectId("5dc6ce16744d1094ab100a97"),
        "Ad" : "Mehmet",
        "Soyad" : "Şahin",
        "Telefon" : "+905333533333",
        "EPosta" : "mehmet.sahin@bilgeadam.com",
        "Adres" : "BilgeAdamBeşiktaş"
}
{
        "_id" : 1,
        "Ad" : "Arif",
        "Soyad" : "Susam",
        "Telefon" : "+905333533333",
        "EPosta" : "arif.susam@bilgeadam.com",
        "Adres" : "BilgeAdamSusam Sokağı"
}
{
        "_id" : ObjectId("5dc6d0b8744d1094ab100a98"),
        "Ad" : "Murat",
        "Soyad" : "Vuranok",
        "Telefon" : "+905333533333",
        "EPosta" : "murat.vuranok@bilgeadam.com",
        "Adres" : "BilgeAdam",
        "Telefonlar" : [
                {
                        "Etiket" : "Cep",
                        "Numara" : "+9055556667788"
                },
                {
                        "Etiket" : "Ev",
                        "Numara" : "+9021256667788"
                },
                {
                        "Etiket" : "İş",
                        "Numara" : "+9021256667799"
                }
        ]
}

*/



db.Kisiler.insert({
    "Ad": "Murat",
    "Soyad": "Vuranok",
    "Telefon": "+905333533333",
    "EPosta": "murat.vuranok@bilgeadam.com",
    "Adres": "BilgeAdam",
    "Telefonlar": [
        {
            "Etiket": "Cep",
            "Numara": "+9055556667788"
        },
        {
            "Etiket": "Ev",
            "Numara": "+9021256667788"
        }
        ,
        {
            "Etiket": "İş",
            "Numara": "+9021256667799"
        }
    ]
})


// Database => Categories (CategoryName,Description , Products (ProductName,Price,UnitsInStock)  

// toplu kayıt ekleme
db.Categories.insertMany([
    {
        "CategoryID": 1,
        "CategoryName": "Beverages",
        "Description": "Soft drinks, coffees, teas, beers, and ales",
        "Products": [
            {
                "ProductId": 1,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    },
    {
        "CategoryID": 2,
        "CategoryName": "Condiments",
        "Description": "Sweet and savory sauces, relishes, spreads, and seasonings",
        "Products": [
            {
                "ProductId": 2,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    },
    {
        "CategoryID": 3,
        "CategoryName": "Confections",
        "Description": "Desserts, candies, and sweet breads",
        "Products": [
            {
                "ProductId": 3,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    },
    {
        "CategoryID": 4, "CategoryName": "Dairy Products",
        "Description": "Cheeses",
        "Products": [
            {
                "ProductId": 4,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    },
    {
        "CategoryID": 5, "CategoryName": "Grains/Cereals",
        "Description": "Breads, crackers, pasta, and cereal",
        "Products": [
            {
                "ProductId": 5,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    },

    {
        "CategoryID": 6, "CategoryName": "Meat/Poultry",
        "Description": "Prepared meats",
        "Products": [
            {
                "ProductId": 6,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    },

    {
        "CategoryID": 7, "CategoryName": "Produce",
        "Description": "Dried fruit and bean curd",
        "Products": [
            {
                "ProductId": 7,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    },
    {
        "CategoryID": 8, "CategoryName": "Seafood",
        "Description": "Seaweed and fish",
        "Products": [
            {
                "ProductId": 8,
                "ProductName": "Ürün 1",
                "Price": 5.00,
                "UnitsInStock": 10
            }
        ]
    }])

// Aradığınız parametreye göre değer getiren sorgu
db.Games.find({ "Kind": "Yetişkin" })
db.Games.find({ "Name": "CAN YELEĞİ" })


db.Games.update({ "Name": "CAN YELEĞİ" }, { $set: { "ImageUrl": "bilge adam" } })
db.Games.update({ "Id": 20 }, { $set: { "ImageUrl": "bilge adam" } })
db.Games.update({ "Id": 177 }, { $set: { "ImageUrl": "bilge adam" } })
db.Games.update({ "Id": 178 }, { $set: { "ImageUrl": "bilge adam" } })
db.Games.update({ "Id": 181 }, { $set: { "ImageUrl": "bilge adam" } })


// tek bir kayıt günceller
db.Games.update({ "ImageUrl": "bilge adam" }, { $set: { "ImageUrl": "www.bilgeadam.com" } })

db.Games.update({ "ImageUrl": "bilge adam" }, { $set: { "ImageUrl": "www.bilgeadam.com" } }, { multi: true })

/*db.Games.find({"ImageUrl":"bilge adam"})
{
        "_id" : ObjectId("5dc6def67e49b1001e002a14"),
        "Id" : 174,
        "Name" : "CAN YELEĞİ",
        "ImageUrl" : "bilge adam",
        "Kind" : "Yetişkin",
        "Url" : "https://sehirtiyatrolari.ibb.istanbul/Activity/Detail/174"
}
*/

// https://docs.mongodb.com/manual/tutorial/insert-documents/

// https://docs.mongodb.com/manual/reference/operator/query/eq/