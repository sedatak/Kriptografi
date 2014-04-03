import math

sayi = int(input("Kontrol edilecek sayiyi giriniz: "))

def asalmi(sayi):

    kok = math.sqrt(sayi)            # Sayının karekökü bulundu.

    if kok == 1:
        return 1
            
    for i in range(2, int(kok) + 1): # İkiden başlayarak kökün bir fazlasına kadar gezer
            
        if asalmi(i)== 1:            # Bölünecek sayılar özyineleme ile kontrol edilir.  

            if (sayi % i == 0):
                return 0             # Sayi asal degildir.
    return 1                         # Sayı asaldır.

if (asalmi(sayi) == 1):
    print("Sayi asaldır.")

else:
    print("Sayi asal degildir.")

