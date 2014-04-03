import math
import random
import binascii

def asalmi(sayi):

    kok = math.sqrt(sayi)            # Sayının karekökü bulundu.

    if kok == 1:
        return 1
            
    for i in range(2, int(kok) + 1): # İkiden başlayarak kökün bir fazlasına kadar gezer
            
        if asalmi(i)== 1:            # Bölünecek sayılar özyineleme ile kontrol edilir.  

            if (sayi % i == 0):
                return 0             # Sayi asal degildir.
    return 1                         # Sayı asaldır.


# Anahtar üretimi

def anahtar_uret(a, b):

    a = random.randint(131441318342695122192609419937146696050066257431720060301523697620149903055663251854220067020503783524785523675819158836547734770656069477,783144131834269512219260941993714669605006625743172006030529504645527800951523697620149903055663251854220067020503783524785523675819158836547734770656069477)
    b = random.randint(131441318342695122192609419937146696050066257431720060301523697620149903055663251854220067020503783524785523675819158836547734770656069477,783144131834269512219260941993714669605006625743172006030529504645527800951523697620149903055663251854220067020503783524785523675819158836547734770656069477)

    asalmi(a)
    while (asalmi(a) == 0):
        a = random.randint(131441318342695122192609419937146696050066257431720060301523697620149903055663251854220067020503783524785523675819158836547734770656069477,783144131834269512219260941993714669605006625743172006030529504645527800951523697620149903055663251854220067020503783524785523675819158836547734770656069477)
        asalmi(a)
    print("2. Asal Sayı", b)

    asalmi(b)
    while (asalmi(b) == 0):
        b = random.randint(131441318342695122192609419937146696050066257431720060301523697620149903055663251854220067020503783524785523675819158836547734770656069477,783144131834269512219260941993714669605006625743172006030529504645527800951523697620149903055663251854220067020503783524785523675819158836547734770656069477)
        asalmi(a)
    print("1. Asal Sayı", a)
    
# Şifreleme

def sifrele():
    x = 0
    p = 1
    q = 1
    anahtar_uret(p, q)
    n = p * q
    print(p, q, n)

    a = 1
    j = 1                               # Jacobi için
    while a < 1100000000:
        if(a*a%n != p):                 # Legendre
            if ( a%n !=0):              # Jacobi 1. şart
                while j < 1100000000:
                    if (j*j == a%p):    # Jacobi 2. şart
                        x = j
                j = j + 1 
        i = i + 1

    plaintext1 = ""
    chippertext = ""
    plaintext1 = input("Şifrelenecek metni giriniz:")
    bin(int.from_bytes(plaintext.encode(), 'big'))
    plaintext = plainttext1[2:]


    t = 1
    y = 1
    while t <5555555555555:
        if (n / t != 0):                 # Aralarında asallık kontrol edilir.
            if (y != 0):
                    chippertext = chippertext + y ** 2 * x **( int(plaintext[i])) % n                 # Asıl şifreleme kısmı
            y = y + 1    
        t = t + 1
    print(chippertext)

# Deşifreleme

def deşifrele():

    plaintext = ""
    chippertext = ""                                             
    chippertext= input("Deşifrelenecek metni giriniz:")                                             

    g = 0
    while g < 555555555555:
        chippertext1 = chippertext1 + int(chippertext[i])           # Quadratic Residue kontrol edilemedi.

    plaintext = chippertext1.to_bytes((chippertext1.bit_length() + 7) // 8, 'big').decode()
    print(plaintext)                        


# main

print("""
Anahtar üretimi için    (1)'e
Şifreleme yapmak için   (2)'ye
Deşifreleme yapmak için (3)'e basınız..
""")
i = int(input(""))


if i == 1:
    anahtar_uret()
elif i == 2:
    sifrele()
elif  i == 3:
    deşifrele()
else:
    print("Lütfen 1, 2 veya 3 giriniz!")
