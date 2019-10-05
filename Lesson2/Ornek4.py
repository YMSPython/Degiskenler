try:
    sayi_bir = int(input("Lütfen bölünecek sayıyı giriniz : "))
    sayi_iki = int(input("Lütfen bölecek olan sayıyı giriniz : "))
    result = sayi_bir / sayi_iki
    print(result)
    # raise Exception("neden işlem düzgün çalıştı :D")
except ValueError as ex:
    print("İşlem hatası ",ex)

except ZeroDivisionError as ex: 
    print("sıfır ", ex) # sıfır  division by zero
else:
    try:
        result = sayi_iki / sayi_bir
        print(result) 
    except ZeroDivisionError as ex:
        print("sıfıra bölünme hatası : ",ex)