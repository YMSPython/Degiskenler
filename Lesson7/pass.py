while True:
    sifre = input("Lütfen bir parola belirleyiniz! : ")
    if not sifre:
        continue
        # pass  # eğer alan boş geçilirse pas geç
    elif len(sifre) in range(3, 8):
        print("Şifreniz : ", sifre)
        break
    else:
        print("parola 8 karakterden uzun, 3 karakterden kısa olmamalıdır.")
