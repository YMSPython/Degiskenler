# Örnek :  Dışarıdan girilen kelimenin uzunluk değeri 8 karakter veya daha uzun bir karekter ise, Onaylandı!, değil ise, Daha uzun bir şifre giriniz.


# len()

pwd = input("Lütfen parolanızı giriniz : ")
if(len(pwd) >= 8):
    print("Parola doğru")
else:
    print("Lütfen bi kaç karakter daha gir zahmet olacak!!")