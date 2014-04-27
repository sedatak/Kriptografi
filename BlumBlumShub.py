import math

def asalmi(sayi):

    kok = math.sqrt(sayi)            # Sayının karekökü bulundu.

    if kok == 1:
        return 1
            
    for i in range(2, int(kok) + 1): # İkiden başlayarak kökün bir fazlasına kadar gezer
            
        if asalmi(i)== 1:            # Bölünecek sayılar özyineleme ile kontrol edilir.  

            if (sayi % i == 0):
                return 0             # Sayi asal degildir.
    return 1                     # Sayı asaldır.


sayi1 = int(input("p: ilk asal sayıyı giriniz: "))

while (asalmi(sayi1) != 1):
    
    sayi1 = int(input("Sayi asal degildir. p değerini tekrar giriniz:"))

sayi2 = int(input("q: ikinci asal sayıyı giriniz: "))

while (asalmi(sayi2) != 1):
    
    sayi2 = int(input("Sayi asal degildir. q değerini tekrar giriniz:"))

M = sayi1 * sayi2

s = int(input("s: seek(tohum) değerini giriniz: "))

sınır = int(input("Kaç rasgelemsi sayı üretilsin: "))

i = 0

while i < sınır:
    c = s**2 % M
    print(c)
    s = c
    i = i + 1

