# Python ile Sayı Tahmin Oyunu Yapımı.
 
from random import randint             # Bu randomu tanımlar.

rand = randint(1, 100)
sayac = 0
 
while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında değer girin :"))


    if(sayi == 0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print(f"Rastele seçilen sayı {rand}!")
        print(f"Tahmin sayınız {sayac}")
 




