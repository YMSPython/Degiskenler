def decorator_metot(metot):
    def sarmal_metot():
        print("Sarmal metot çalıştı! {}'metodundan önce".format(metot.__name__))
        return metot()
    return sarmal_metot



@decorator_metot
def PrinterMetot():
    print("Printer Metodu Çalıştı!!!")



PrinterMetot()
