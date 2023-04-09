# Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan Python örneği:
'''

def dikdortgen(genis, yuksek):
    alan = genis * yuksek
    print('alan : ', alan)


g = int(input('genişlik : '))
y = int(input('yukseklik : '))

dikdortgen(g, y)

'''


def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) * float(yukseklik)
    print ("Alan :",alan)
    return alan
 
gen = input("Genişlik :")
 
yuk = input("Yükseklik : ")
 
dikdortgenAlan(gen, yuk)
 



