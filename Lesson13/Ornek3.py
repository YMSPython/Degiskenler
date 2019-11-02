class Ogrenci:
    """
    self : sınıf içerisinde yer alan metotların diğerlerinden farkı hangi sınıf içerisinden çalıştığını  belirtmesidir
    """
    Adi = ""

    def Kaydet(self):
        print(self.Adi,"Adlı Öğrencinin Giriş İşlemleri Yapıldı")

    def NotVer(self, ogrenci_not):
        print(ogrenci_not, "Adlı öğrenciye not verildi")

    def CezaVer(self, ogrenci_ceza):
        print(ogrenci_ceza, "Adlı öğrenciye ceza verildi")

    def YoklamaGir(self, ogrenci_yoklama):
        print(ogrenci_yoklama, "Adlı öğrecinin yoklaması girildi")


ogr = Ogrenci()
ogr.Adi = "Murat Vuranok"
ogr.CezaVer("Murat Vuranok")
ogr.Kaydet()

Ogrenci.CezaVer("", "Murat Vuranok")
Ogrenci.YoklamaGir("","Murat Vuranok")

 