metin = "BilgE Adam"
print(metin.lower())
print(metin.upper())

elemanlar = [
    {
        "FirstName": "Murat",
        "LastName": "Vuranok",
        "Mail": "murat.vuranok@bilgeadam.com"
    },
    {
        "FirstName": "Murat",
        "LastName": "Vuranok",
        "Mail": "murat.vuranok@bilgeadam.com"
    }
]

for x in elemanlar:
    for x, y in x.items():
        print("{0:<15}: {1}".format(x, y))
