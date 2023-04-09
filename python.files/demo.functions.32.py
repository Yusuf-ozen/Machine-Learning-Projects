# 1 - Gönderilen bir kelimeyi belirtilen kez ekranda gösteren bir fonksiyon yazınız.

"""

kelime = input("Enter :  ")
adet = int(input("Enter num : "))

def yazdir(kelime, adet):            # bu şekilde yaptığında adet defa kelimeyi yazdırır
    print(kelime * adet)


yazdir(kelime, adet)




def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("yusuf\n",5)     # burada da aynı şekilde yazdırır.


"""



# 2 - Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazınız.



def listeyeCevir(*params):      # Buradaki yıldız sınırsız sayıyı ifade eder.
    liste = []


    for param in params:
        liste.append(param)

    return liste


result = listeyeCevir(10, 20, 30, "merhaba")
print(result)



# 3 - Gönderilen iki sayı arasındaki asal sayıları bulan bir fonksiyon yazınız.

"""

ilk = int(input("ilk :  "))
son = int(input("son :  "))


def asal(ilk, son):
    for x in range(ilk, son + 1):
        if (x > 1):
            for i in range(2, x):
                if (x % i == 0):
                    break
                
            else:
                print(x)


asal(ilk, son)

"""

# 4 - Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

sayi = int(input("Sayi :  "))


def tambolen(sayi):
    tam = []


    for i in range(2, sayi + 1):
        if (sayi % i == 0):
            tam.append(i)

        
    return tam

print(tambolen(sayi))




