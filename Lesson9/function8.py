# Kullanıcı dışarıdan isim soyisim ve domain adresi girecek
# 'murat','vuranok','bilgeadam.com'
# murat.vuranok@bilgeadam.com

# eğer kullanıcı, domain adı girmezse, default olarak bilgeadam.com dönsün


def Mail(firstname: str, lastname: str, domain: str = 'bilgeadam.com') -> str:
    return "{}.{}@{}".format(firstname,lastname, domain)

#print(Mail('murat','vuranok'))
# murat.vuranok@bilgeadam.com

# print(type(Mail('','')))

# <class 'str'>

print("Mail metodunun geriye dönüş tipi", Mail.__annotations__)
# Mail metodunun geriye dönüş tipi {'firstname': <class 'str'>, 'lastname': <class 'str'>, 'domain': <class 'str'>}
# Mail metodunun geriye dönüş tipi {'firstname': <class 'str'>, 'lastname': <class 'str'>, 'domain': <class 'str'>, 'return': <class 'str'>}
 