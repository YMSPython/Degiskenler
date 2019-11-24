# alias python=/usr/local/bin/python3

import pymongo
import ssl

# myClient = pymongo.MongoClient(
#     "mongodb+srv://admin:Hflgp4O8PaVhEiro@cluster0-tw4uy.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)

# myDb = myClient["PhoneBook"]
# myCollection = myDb["People"]

# people = myCollection.find()


class Person:
    def __str__(self):
        return "{} {} {} {}".format(self.FirstName, self.LastName, self.Mail, self.Phone)


def Create():
    person = Person()
    person.FirstName = input("Lütfen Adınızı Giriniz : ")
    person.LastName = input("Lütfen Soyadınızı Giriniz : ")
    person.Mail = input("Lütfen Mail Adresinizi Giriniz : ")
    person.Phone = input("Lütfen Telefon Numaranızı Giriniz : ")
    return person.__dict__


def ConnectClient():
    return pymongo.MongoClient(
        "mongodb+srv://admin:Hflgp4O8PaVhEiro@cluster0-tw4uy.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)


def Insert(person):
    myClient = ConnectClient()
    myDb = myClient["PhoneBook"]
    myCollection = myDb["People"]
    myCollection.insert_one(person)

def List():
    myClient = ConnectClient()
    myDb = myClient["PhoneBook"]
    myCollection = myDb["People"]
    people = myCollection.find()

    for i in people:
        for x, y in i.items():
            print("{0:<10} : {1}".format(x, y))
        print("-"*60)


def Delete(param):
    myClient = ConnectClient()
    myDb = myClient["PhoneBook"]
    myCollection = myDb["People"]
    myQuery = {"FirstName": param}
    myCollection.delete_one(myQuery)


def Update(param):
    myClint = ConnectClient()
    myDb = myClint["PhoneBook"]
    myCollection = myDb["People"]
    myQuery = {"FirstName": param}

    per = Create()

    newValue = {"$set": per}
    myCollection.update_one(myQuery, newValue)


def Start():

    title = """
 ____                                     ______    __    ___             
/\  _`\                                  /\__  _\__/\ \__/\_ \            
\ \ \L\_\ __      ___     ___   __  __   \/_/\ \/\_\ \ ,_\//\ \      __   
 \ \  _\/'__`\  /' _ `\  /'___\/\ \/\ \     \ \ \/\ \ \ \/ \ \ \   /'__`\ 
  \ \ \/\ \L\.\_/\ \/\ \/\ \__/\ \ \_\ \     \ \ \ \ \ \ \_ \_\ \_/\  __/ 
   \ \_\ \__/.\_\ \_\ \_\ \____\\/`____ \     \ \_\ \_\ \__\/\____\ \____"\"
    \/_/\/__/\/_/\/_/\/_/\/____/ `/___/> \     \/_/\/_/\/__/\/____/\/____/
                                    /\___/                                
                                    \/__/ """
    print(title)
    key = "y"

    while key != "e":
        key = input("""
------------------------------
- Silme      işlemi için (d) - 
- Ekleme     işlemi için (a) -
- Listeleme  işlemi için (l) -
- Güncelleme işlemi için (u) -
------------------------------
- Çıkış      işlemi için (e) -
------------------------------

Lütfen İşlem Seçiniz : """).lower()

        if key == "a":
            per = Create() 
            Insert(per)
        elif key == "l":
            List()
        elif key == "d":
            firstname = input("Lütfen silmek istediğiniz kişinin adını giriniz : ")
            Delete(firstname)
            List()
        elif key == "u":
            firstname = input("Lütfen güncellemek istediğiniz kişinin adını giriniz : ") 
            Update(firstname)
    else:
        print("Bilge Adam Telefon Rehberinden Çıkış Yaptınız!")

Start()
