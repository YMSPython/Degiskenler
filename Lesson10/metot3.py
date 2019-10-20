def MetotVol1(Ad, Soyad, Telefon, Gorev, *params):
    print(Ad, Soyad, Telefon, Gorev, " ".join(params))


#MetotVol1('Murat', 'Vuranok', '+905323520000', 'Danışman', 'Bilge Adam', 'Bilge Hatun')


def MetotVol2(*params):
    for p in params:
        print(p)


# MetotVol2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


def MetotVol3(**params):
    for p in params:
        print("{0:<15}: {1}".format(p,params[p]))


MetotVol3(
    FirstName = 'Murat',
    LastName = 'Vuranok',
    Phone = '+905324445566',
    Mail = 'murat.vuranok@bilgeadam.com')
