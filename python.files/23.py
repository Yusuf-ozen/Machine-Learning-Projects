# Kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulan Python örneği. Sayının çift olup olmadığı fonksiyon ile kontrol ediliyor.


'''

# Fonksiyonsuz yazımı

ilk = int(input('İlk sayı :  '))
son = int(input('Son sayı :  '))
sayac = 0
top = 0



for sayi in range(ilk, son):
    if (sayi % 2 == 0):
        print(sayi)
        sayac += 1
        top += sayi

average = top / sayac
print('Toplam : ', top)
print('Ortalama : ', average)

'''



ilk = int(input('İlk sayı :  '))
son = int(input('Son sayı :  '))

sayac = 0
top = 0


def cift(sayi):
    return (sayi % 2 == 0)


for x in range(ilk, son):
    if cift(x):
        print(x)
        top += x
        sayac += 1

average = top / sayac

print('toplam : ', top)
print('ortalama : ', average)
