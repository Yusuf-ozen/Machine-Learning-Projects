"""

def daireAlan(yaricap):                             # parantez içine yazdığınla işlem yapılır
    alan = yaricap * yaricap * 3.14
    
    print ("Alan :  ",alan)

    return alan
 
r = float(input("Yarıçapı Gir :  "))
 
daireAlan(r)

"""

"""

def alan(yukseklik, genislik):

    alan = yukseklik * genislik

    print("Alan :  ",alan)

    return alan



a = float(input("Yuksekligi giriniz :  "))
b = float(input("Genisligi giriniz :  "))


alan(a, b)


"""



# toplam = 0
# sayac = 0

# ustSinir = int(input("üst sayıyi girirniz :  "))
# AltSinir = int(input("altt sayıyi girirniz :  "))



# for x in range(AltSinir, ustSinir):
#     if (x % 2 == 0):
#         print(x)
#         toplam += x
#         sayac += 1


# average = toplam / sayac

# print("toplam :  ", toplam)
# print("ortalama >>>  ",average)






def cift(x):

   return x % 2 == 0



toplam = 0
sayac = 0

AltSinir = int(input("Altsinir  :  "))
UstSinir = int(input("Ustsinir  :  "))



for y in range(AltSinir, UstSinir):      # burada ustsınırdan sonra virgul koyup 2 yazabilirsin.

    if (cift(int(y))):                       # Burada üstteki fonksiyonu kullanabiliriz.
        print(y)
        toplam += y
        sayac += 1



ortalama = (toplam/sayac)

print("Toplam : ", toplam)
print("ortalama : ", ortalama)



