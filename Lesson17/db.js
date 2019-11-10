// database oluştur
use Northwind

// tablo oluştur ve kayıt ekle

db.Products.insertMany([{
    "ProductID": 1,
    "ProductName": "Chai",
    "CategoryID": 1,
    "UnitPrice": 18.00,
    "UnitsInStock": 39
  },
  {
    "ProductID": 2,
    "ProductName": "Chang",
    "CategoryID": 1,
    "UnitPrice": 19.00,
    "UnitsInStock": 17
  },
  {
    "ProductID": 3,
    "ProductName": "Aniseed Syrup",
    "CategoryID": 2,
    "UnitPrice": 10.00,
    "UnitsInStock": 13
  },
  {
    "ProductID": 4,
    "ProductName": "Chef Anton's Cajun Seasoning",
    "CategoryID": 2,
    "UnitPrice": 22.00,
    "UnitsInStock": 53
  },
  {
    "ProductID": 5,
    "ProductName": "Chef Anton's Gumbo Mix",
    "CategoryID": 2,
    "UnitPrice": 21.35,
    "UnitsInStock": 0
  },
  {
    "ProductID": 6,
    "ProductName": "Grandma's Boysenberry Spread",
    "CategoryID": 2,
    "UnitPrice": 25.00,
    "UnitsInStock": 120
  },
  {
    "ProductID": 7,
    "ProductName": "Uncle Bob's Organic Dried Pears",
    "CategoryID": 7,
    "UnitPrice": 30.00,
    "UnitsInStock": 15
  },
  {
    "ProductID": 8,
    "ProductName": "Northwoods Cranberry Sauce",
    "CategoryID": 2,
    "UnitPrice": 40.00,
    "UnitsInStock": 6
  },
  {
    "ProductID": 9,
    "ProductName": "Mishi Kobe Niku",
    "CategoryID": 6,
    "UnitPrice": 97.00,
    "UnitsInStock": 29
  },
  {
    "ProductID": 10,
    "ProductName": "Ikura",
    "CategoryID": 8,
    "UnitPrice": 31.00,
    "UnitsInStock": 31
  },
  {
    "ProductID": 11,
    "ProductName": "Queso Cabrales",
    "CategoryID": 4,
    "UnitPrice": 21.00,
    "UnitsInStock": 22
  },
  {
    "ProductID": 12,
    "ProductName": "Queso Manchego La Pastora",
    "CategoryID": 4,
    "UnitPrice": 38.00,
    "UnitsInStock": 86
  },
  {
    "ProductID": 13,
    "ProductName": "Konbu",
    "CategoryID": 8,
    "UnitPrice": 6.00,
    "UnitsInStock": 24
  },
  {
    "ProductID": 14,
    "ProductName": "Tofu",
    "CategoryID": 7,
    "UnitPrice": 23.25,
    "UnitsInStock": 35
  },
  {
    "ProductID": 15,
    "ProductName": "Genen Shouyu",
    "CategoryID": 2,
    "UnitPrice": 15.50,
    "UnitsInStock": 39
  },
  {
    "ProductID": 16,
    "ProductName": "Pavlova",
    "CategoryID": 3,
    "UnitPrice": 17.45,
    "UnitsInStock": 29
  },
  {
    "ProductID": 17,
    "ProductName": "Alice Mutton",
    "CategoryID": 6,
    "UnitPrice": 39.00,
    "UnitsInStock": 0
  },
  {
    "ProductID": 18,
    "ProductName": "Carnarvon Tigers",
    "CategoryID": 8,
    "UnitPrice": 62.50,
    "UnitsInStock": 42
  },
  {
    "ProductID": 19,
    "ProductName": "Teatime Chocolate Biscuits",
    "CategoryID": 3,
    "UnitPrice": 9.20,
    "UnitsInStock": 25
  },
  {
    "ProductID": 20,
    "ProductName": "Sir Rodney's Marmalade",
    "CategoryID": 3,
    "UnitPrice": 81.00,
    "UnitsInStock": 40
  },
  {
    "ProductID": 21,
    "ProductName": "Sir Rodney's Scones",
    "CategoryID": 3,
    "UnitPrice": 10.00,
    "UnitsInStock": 3
  },
  {
    "ProductID": 22,
    "ProductName": "Gustaf's Knäckebröd",
    "CategoryID": 5,
    "UnitPrice": 21.00,
    "UnitsInStock": 104
  },
  {
    "ProductID": 23,
    "ProductName": "Tunnbröd",
    "CategoryID": 5,
    "UnitPrice": 9.00,
    "UnitsInStock": 61
  },
  {
    "ProductID": 24,
    "ProductName": "Guaraná Fantástica",
    "CategoryID": 1,
    "UnitPrice": 4.50,
    "UnitsInStock": 20
  },
  {
    "ProductID": 25,
    "ProductName": "NuNuCa Nuß-Nougat-Creme",
    "CategoryID": 3,
    "UnitPrice": 14.00,
    "UnitsInStock": 76
  },
  {
    "ProductID": 26,
    "ProductName": "Gumbär Gummibärchen",
    "CategoryID": 3,
    "UnitPrice": 31.23,
    "UnitsInStock": 15
  },
  {
    "ProductID": 27,
    "ProductName": "Schoggi Schokolade",
    "CategoryID": 3,
    "UnitPrice": 43.90,
    "UnitsInStock": 49
  },
  {
    "ProductID": 28,
    "ProductName": "Rössle Sauerkraut",
    "CategoryID": 7,
    "UnitPrice": 45.60,
    "UnitsInStock": 26
  },
  {
    "ProductID": 29,
    "ProductName": "Thüringer Rostbratwurst",
    "CategoryID": 6,
    "UnitPrice": 123.79,
    "UnitsInStock": 0
  },
  {
    "ProductID": 30,
    "ProductName": "Nord-Ost Matjeshering",
    "CategoryID": 8,
    "UnitPrice": 25.89,
    "UnitsInStock": 10
  },
  {
    "ProductID": 31,
    "ProductName": "Gorgonzola Telino",
    "CategoryID": 4,
    "UnitPrice": 12.50,
    "UnitsInStock": 0
  },
  {
    "ProductID": 32,
    "ProductName": "Mascarpone Fabioli",
    "CategoryID": 4,
    "UnitPrice": 32.00,
    "UnitsInStock": 9
  },
  {
    "ProductID": 33,
    "ProductName": "Geitost",
    "CategoryID": 4,
    "UnitPrice": 2.50,
    "UnitsInStock": 112
  },
  {
    "ProductID": 34,
    "ProductName": "Sasquatch Ale",
    "CategoryID": 1,
    "UnitPrice": 14.00,
    "UnitsInStock": 111
  },
  {
    "ProductID": 35,
    "ProductName": "Steeleye Stout",
    "CategoryID": 1,
    "UnitPrice": 18.00,
    "UnitsInStock": 20
  },
  {
    "ProductID": 36,
    "ProductName": "Inlagd Sill",
    "CategoryID": 8,
    "UnitPrice": 19.00,
    "UnitsInStock": 112
  },
  {
    "ProductID": 37,
    "ProductName": "Gravad lax",
    "CategoryID": 8,
    "UnitPrice": 26.00,
    "UnitsInStock": 11
  },
  {
    "ProductID": 38,
    "ProductName": "Côte de Blaye",
    "CategoryID": 1,
    "UnitPrice": 263.50,
    "UnitsInStock": 17
  },
  {
    "ProductID": 39,
    "ProductName": "Chartreuse verte",
    "CategoryID": 1,
    "UnitPrice": 18.00,
    "UnitsInStock": 69
  },
  {
    "ProductID": 40,
    "ProductName": "Boston Crab Meat",
    "CategoryID": 8,
    "UnitPrice": 18.40,
    "UnitsInStock": 123
  },
  {
    "ProductID": 41,
    "ProductName": "Jack's New England Clam Chowder",
    "CategoryID": 8,
    "UnitPrice": 9.65,
    "UnitsInStock": 85
  },
  {
    "ProductID": 42,
    "ProductName": "Singaporean Hokkien Fried Mee",
    "CategoryID": 5,
    "UnitPrice": 14.00,
    "UnitsInStock": 26
  },
  {
    "ProductID": 43,
    "ProductName": "Ipoh Coffee",
    "CategoryID": 1,
    "UnitPrice": 46.00,
    "UnitsInStock": 17
  },
  {
    "ProductID": 44,
    "ProductName": "Gula Malacca",
    "CategoryID": 2,
    "UnitPrice": 19.45,
    "UnitsInStock": 27
  },
  {
    "ProductID": 45,
    "ProductName": "Rogede sild",
    "CategoryID": 8,
    "UnitPrice": 9.50,
    "UnitsInStock": 5
  },
  {
    "ProductID": 46,
    "ProductName": "Spegesild",
    "CategoryID": 8,
    "UnitPrice": 12.00,
    "UnitsInStock": 95
  },
  {
    "ProductID": 47,
    "ProductName": "Zaanse koeken",
    "CategoryID": 3,
    "UnitPrice": 9.50,
    "UnitsInStock": 36
  },
  {
    "ProductID": 48,
    "ProductName": "Chocolade",
    "CategoryID": 3,
    "UnitPrice": 12.75,
    "UnitsInStock": 15
  },
  {
    "ProductID": 49,
    "ProductName": "Maxilaku",
    "CategoryID": 3,
    "UnitPrice": 20.00,
    "UnitsInStock": 10
  },
  {
    "ProductID": 50,
    "ProductName": "Valkoinen suklaa",
    "CategoryID": 3,
    "UnitPrice": 16.25,
    "UnitsInStock": 65
  },
  {
    "ProductID": 51,
    "ProductName": "Manjimup Dried Apples",
    "CategoryID": 7,
    "UnitPrice": 53.00,
    "UnitsInStock": 20
  },
  {
    "ProductID": 52,
    "ProductName": "Filo Mix",
    "CategoryID": 5,
    "UnitPrice": 7.00,
    "UnitsInStock": 38
  },
  {
    "ProductID": 53,
    "ProductName": "Perth Pasties",
    "CategoryID": 6,
    "UnitPrice": 32.80,
    "UnitsInStock": 0
  },
  {
    "ProductID": 54,
    "ProductName": "Tourtière",
    "CategoryID": 6,
    "UnitPrice": 7.45,
    "UnitsInStock": 21
  },
  {
    "ProductID": 55,
    "ProductName": "Pâté chinois",
    "CategoryID": 6,
    "UnitPrice": 24.00,
    "UnitsInStock": 115
  },
  {
    "ProductID": 56,
    "ProductName": "Gnocchi di nonna Alice",
    "CategoryID": 5,
    "UnitPrice": 38.00,
    "UnitsInStock": 21
  },
  {
    "ProductID": 57,
    "ProductName": "Ravioli Angelo",
    "CategoryID": 5,
    "UnitPrice": 19.50,
    "UnitsInStock": 36
  },
  {
    "ProductID": 58,
    "ProductName": "Escargots de Bourgogne",
    "CategoryID": 8,
    "UnitPrice": 13.25,
    "UnitsInStock": 62
  },
  {
    "ProductID": 59,
    "ProductName": "Raclette Courdavault",
    "CategoryID": 4,
    "UnitPrice": 55.00,
    "UnitsInStock": 79
  },
  {
    "ProductID": 60,
    "ProductName": "Camembert Pierrot",
    "CategoryID": 4,
    "UnitPrice": 34.00,
    "UnitsInStock": 19
  },
  {
    "ProductID": 61,
    "ProductName": "Sirop d'érable",
    "CategoryID": 2,
    "UnitPrice": 28.50,
    "UnitsInStock": 113
  },
  {
    "ProductID": 62,
    "ProductName": "Tarte au sucre",
    "CategoryID": 3,
    "UnitPrice": 49.30,
    "UnitsInStock": 17
  },
  {
    "ProductID": 63,
    "ProductName": "Vegie-spread",
    "CategoryID": 2,
    "UnitPrice": 43.90,
    "UnitsInStock": 24
  },
  {
    "ProductID": 64,
    "ProductName": "Wimmers gute Semmelknödel",
    "CategoryID": 5,
    "UnitPrice": 33.25,
    "UnitsInStock": 22
  },
  {
    "ProductID": 65,
    "ProductName": "Louisiana Fiery Hot Pepper Sauce",
    "CategoryID": 2,
    "UnitPrice": 21.05,
    "UnitsInStock": 76
  },
  {
    "ProductID": 66,
    "ProductName": "Louisiana Hot Spiced Okra",
    "CategoryID": 2,
    "UnitPrice": 17.00,
    "UnitsInStock": 4
  },
  {
    "ProductID": 67,
    "ProductName": "Laughing Lumberjack Lager",
    "CategoryID": 1,
    "UnitPrice": 14.00,
    "UnitsInStock": 52
  },
  {
    "ProductID": 68,
    "ProductName": "Scottish Longbreads",
    "CategoryID": 3,
    "UnitPrice": 12.50,
    "UnitsInStock": 6
  },
  {
    "ProductID": 69,
    "ProductName": "Gudbrandsdalsost",
    "CategoryID": 4,
    "UnitPrice": 36.00,
    "UnitsInStock": 26
  },
  {
    "ProductID": 70,
    "ProductName": "Outback Lager",
    "CategoryID": 1,
    "UnitPrice": 15.00,
    "UnitsInStock": 15
  },
  {
    "ProductID": 71,
    "ProductName": "Flotemysost",
    "CategoryID": 4,
    "UnitPrice": 21.50,
    "UnitsInStock": 26
  },
  {
    "ProductID": 72,
    "ProductName": "Mozzarella di Giovanni",
    "CategoryID": 4,
    "UnitPrice": 34.80,
    "UnitsInStock": 14
  },
  {
    "ProductID": 73,
    "ProductName": "Röd Kaviar",
    "CategoryID": 8,
    "UnitPrice": 15.00,
    "UnitsInStock": 101
  },
  {
    "ProductID": 74,
    "ProductName": "Longlife Tofu",
    "CategoryID": 7,
    "UnitPrice": 10.00,
    "UnitsInStock": 4
  },
  {
    "ProductID": 75,
    "ProductName": "Rhönbräu Klosterbier",
    "CategoryID": 1,
    "UnitPrice": 7.75,
    "UnitsInStock": 125
  },
  {
    "ProductID": 76,
    "ProductName": "Lakkalikööri",
    "CategoryID": 1,
    "UnitPrice": 18.00,
    "UnitsInStock": 57
  },
  {
    "ProductID": 77,
    "ProductName": "Original Frankfurter grüne Soße",
    "CategoryID": 2,
    "UnitPrice": 13.00,
    "UnitsInStock": 32
  }])