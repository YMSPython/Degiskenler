# .startswith()  => nesne parametrede gönderdiğiniz değer ile başlayıp başlamadığını kontrol eder var ise Turue, yok ise False değerini teslim eder


# .endswith()  => nesne parametrede gönderdiğiniz değer ile bitip bitmediğini kontrol eder var ise Turue, yok ise False değerini teslim eder

 
metin = "bilge adam"
result = metin.startswith("bilge")

print("kelime bilge ile başlamaktadır" if result else "kelime bilge ile başlamamaktadır")

result = metin.endswith("adam")
print("kelime adam ile bitmektedir" if result else "kelime bilge ile bitmemektedir")