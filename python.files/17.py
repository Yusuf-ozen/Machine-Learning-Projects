# Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan Python örneği:

'''
yaricap = int(input('Yaricapi giriniz : '))


def alanHesapla(r):
    pi = 3.141
    alan = pi * r**2


    print('alan : ', alan)


alanHesapla(yaricap)

'''






def alanHesapla(r):
    alan = r * r * 3.14
    print(alan)

    return alan


yaricap = int(input('yarıçap :  '))

alanHesapla(yaricap)


