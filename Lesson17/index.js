// bir tablo içerisinde veri silmek için
// 1) use DatabaseName
// 2) db."Tablo - Collection".remove({"key":"value"})


// bir veri tabanından Table(Collection) silmek için 
// 1) use DatabaseName
// 2) db."Tablo - Collection".drop()


// server üzerinden bir database silmek için
// use DatabaseName
// db.dropDatabase()

// Northwind => Products

// 1) Equality == 

// db.Products.find({"ProductID" : 77}) 
// Kategori Id değeri 8 olan ürünlerin listelenmesi
// db.Products.find({"CategoryID" : 8})


// 2) Less Than <

// ürün bedeli $50 dan az olanların listelenmesi
// db.Products.find({"UnitPrice":{ $lt : 50}}).pretty()


// 3) Grather Than >
// Ürün bedeli $100 dan fazla olanların listelenmesi
// db.Products.find({"UnitPrice":{ $gt : 100}}).pretty()



// 4) Grather Than and Equal >= 
// db.Products.find({"UnitPrice":{ $gte : 13}}).sort({"UnitPrice": 1}).pretty()

// 5) Sort ( Sql => Order By ) Ascending (1) ( asc - Fakirden Zengine A'dan Z'ye, 0'dan 9'a ) - Descending (-1) ( desc - Zenginden Fakire Z'den A'a , 9'dan 0'a )


// Artan Sırada 1
// db.Products.find({"UnitPrice":{ $lt : 50}}).sort({"UnitPrice" : 1})

// Azalan Sırada -1
// db.Products.find({"UnitPrice":{ $lt : 50}}).sort({"UnitPrice" : -1})


// Not Equal != 

// db.Products.find({"UnitPrice":{ $ne : 13}}).sort({"UnitPrice": 1}).pretty()
// db.Products.find({"CategoryID":{ $ne : 1}}).sort({"CategoryID": 1}).pretty()


// and ve or kullanımı

db.Products.find({
    $and: [
        {
            "CategoryID":
            {
                $gte: 3
            }
        },
        {
            "CategoryID":
            {
                $lte: 6
            }
        }
    ]
}).sort({
    "CategoryID": 1
}).pretty()







// Fiyatı 100$ büyük veya stok adedi 100 den küçük olan ürünlerin listelenmesi
db.Products.find(
    {
        $or:
            [
                {
                    "UnitsInStock": { $lte: 100 }
                },
                {
                    "UnitPrice": { $gte: 100 }
                }
            ]
    },
    {
        ProductName: 1,
        UnitPrice: 1,
        _id: 0
    }
).sort(
    {
        "UnitsInStock": 1
    }
).pretty()


db.Products.find({}, { ProductName: 1, _id: 0 })



// 100 hatası => dbpath bulunamadı   çözüm :) mongod --dbpath ~/data/db
// 48 hatası  => port kullanımda     çözüm :) npx kill-port 27017

// Yukarıdaki çalışmazsa :)
// sudo lsof -iTCP -sTCP:LISTEN -n -P
// sudo kill PINID


db.Categories.insertMany([{
    "CategoryID": 1,
    "CategoryName": "Beverages",
    "Description": "Soft drinks, coffees, teas, beers, and ales"
},
{
    "CategoryID": 2,
    "CategoryName": "Condiments",
    "Description": "Sweet and savory sauces, relishes, spreads, and seasonings"
},
{
    "CategoryID": 3,
    "CategoryName": "Confections",
    "Description": "Desserts, candies, and sweet breads"
},
{
    "CategoryID": 4,
    "CategoryName": "Dairy Products",
    "Description": "Cheeses"
},
{
    "CategoryID": 5,
    "CategoryName": "Grains/Cereals",
    "Description": "Breads, crackers, pasta, and cereal"
},
{
    "CategoryID": 6,
    "CategoryName": "Meat/Poultry",
    "Description": "Prepared meats"
},
{
    "CategoryID": 7,
    "CategoryName": "Produce",
    "Description": "Dried fruit and bean curd"
},
{
    "CategoryID": 8,
    "CategoryName": "Seafood",
    "Description": "Seaweed and fish"
}])




db.Categories.aggregate(
    {
        $lookup: {
            from: "Products",
            localField: "CategoryID",
            foreignField: "CategoryID",
            as: "Products"
        }
    }
).pretty()


{
    "_id" : ObjectId("5dc82cd6953c45e1daabe58c"),
        "CategoryID" : 8,
            "CategoryName" : "Seafood",
                "Description" : "Seaweed and fish",
                    "Products" : [
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe541"),
                            "ProductID": 10,
                            "ProductName": "Ikura",
                            "CategoryID": 8,
                            "UnitPrice": 31,
                            "UnitsInStock": 31
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe544"),
                            "ProductID": 13,
                            "ProductName": "Konbu",
                            "CategoryID": 8,
                            "UnitPrice": 6,
                            "UnitsInStock": 24
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe549"),
                            "ProductID": 18,
                            "ProductName": "Carnarvon Tigers",
                            "CategoryID": 8,
                            "UnitPrice": 62.5,
                            "UnitsInStock": 42
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe555"),
                            "ProductID": 30,
                            "ProductName": "Nord-Ost Matjeshering",
                            "CategoryID": 8,
                            "UnitPrice": 25.89,
                            "UnitsInStock": 10
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe55b"),
                            "ProductID": 36,
                            "ProductName": "Inlagd Sill",
                            "CategoryID": 8,
                            "UnitPrice": 19,
                            "UnitsInStock": 112
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe55c"),
                            "ProductID": 37,
                            "ProductName": "Gravad lax",
                            "CategoryID": 8,
                            "UnitPrice": 26,
                            "UnitsInStock": 11
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe55f"),
                            "ProductID": 40,
                            "ProductName": "Boston Crab Meat",
                            "CategoryID": 8,
                            "UnitPrice": 18.4,
                            "UnitsInStock": 123
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe560"),
                            "ProductID": 41,
                            "ProductName": "Jack's New England Clam Chowder",
                            "CategoryID": 8,
                            "UnitPrice": 9.65,
                            "UnitsInStock": 85
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe564"),
                            "ProductID": 45,
                            "ProductName": "Rogede sild",
                            "CategoryID": 8,
                            "UnitPrice": 9.5,
                            "UnitsInStock": 5
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe565"),
                            "ProductID": 46,
                            "ProductName": "Spegesild",
                            "CategoryID": 8,
                            "UnitPrice": 12,
                            "UnitsInStock": 95
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe571"),
                            "ProductID": 58,
                            "ProductName": "Escargots de Bourgogne",
                            "CategoryID": 8,
                            "UnitPrice": 13.25,
                            "UnitsInStock": 62
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe580"),
                            "ProductID": 73,
                            "ProductName": "Röd Kaviar",
                            "CategoryID": 8,
                            "UnitPrice": 15,
                            "UnitsInStock": 101
                        }
                    ]
}




db.Categories.aggregate(
    {
        $match: {
            "CategoryID": 1
        }
    },
    {
        $lookup: {
            from: "Products",
            localField: "CategoryID",
            foreignField: "CategoryID",
            as: "Products"
        }
    }
).pretty()


{
    "_id" : ObjectId("5dc82cd6953c45e1daabe585"),
        "CategoryID" : 1,
            "CategoryName" : "Beverages",
                "Description" : "Soft drinks, coffees, teas, beers, and ales",
                    "Products" : [
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe538"),
                            "ProductID": 1,
                            "ProductName": "Chai",
                            "CategoryID": 1,
                            "UnitPrice": 18,
                            "UnitsInStock": 39
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe539"),
                            "ProductID": 2,
                            "ProductName": "Chang",
                            "CategoryID": 1,
                            "UnitPrice": 19,
                            "UnitsInStock": 17
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe54f"),
                            "ProductID": 24,
                            "ProductName": "Guaraná Fantástica",
                            "CategoryID": 1,
                            "UnitPrice": 4.5,
                            "UnitsInStock": 20
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe559"),
                            "ProductID": 34,
                            "ProductName": "Sasquatch Ale",
                            "CategoryID": 1,
                            "UnitPrice": 14,
                            "UnitsInStock": 111
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe55a"),
                            "ProductID": 35,
                            "ProductName": "Steeleye Stout",
                            "CategoryID": 1,
                            "UnitPrice": 18,
                            "UnitsInStock": 20
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe55d"),
                            "ProductID": 38,
                            "ProductName": "Côte de Blaye",
                            "CategoryID": 1,
                            "UnitPrice": 263.5,
                            "UnitsInStock": 17
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe55e"),
                            "ProductID": 39,
                            "ProductName": "Chartreuse verte",
                            "CategoryID": 1,
                            "UnitPrice": 18,
                            "UnitsInStock": 69
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe562"),
                            "ProductID": 43,
                            "ProductName": "Ipoh Coffee",
                            "CategoryID": 1,
                            "UnitPrice": 46,
                            "UnitsInStock": 17
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe57a"),
                            "ProductID": 67,
                            "ProductName": "Laughing Lumberjack Lager",
                            "CategoryID": 1,
                            "UnitPrice": 14,
                            "UnitsInStock": 52
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe57d"),
                            "ProductID": 70,
                            "ProductName": "Outback Lager",
                            "CategoryID": 1,
                            "UnitPrice": 15,
                            "UnitsInStock": 15
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe582"),
                            "ProductID": 75,
                            "ProductName": "Rhönbräu Klosterbier",
                            "CategoryID": 1,
                            "UnitPrice": 7.75,
                            "UnitsInStock": 125
                        },
                        {
                            "_id": ObjectId("5dc80e23953c45e1daabe583"),
                            "ProductID": 76,
                            "ProductName": "Lakkalikööri",
                            "CategoryID": 1,
                            "UnitPrice": 18,
                            "UnitsInStock": 57
                        }
                    ]
}
 

db.Categories.insert({
    "CategoryName": "",
    "Description": ""
})