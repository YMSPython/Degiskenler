class Employee:
    """
    Açıklama alanı ekleyebilirsiniz 
    bu satırları görüntülemek için, .__doc__ nesnesini kullanabilirsiniz

    FirstName : Kişinin Adı
    LastName  : Kişinin Soyadı
    Phone     : Kişinin Telefonu
    Mail      : Kişinin Maili
    """


# yeni bir örnek alma (new instance)
personel = Employee()
# print(personel.__doc__)

personel.FirstName = "Murat"
personel.LastName  = "Vuranok"
personel.Mail      = "murat.vuranok@bilgeadam.com"
personel.Phone     = "+905323567890"


# print(personel)
# <__main__.Employee object at 0x102990f28>
print(personel.FirstName)