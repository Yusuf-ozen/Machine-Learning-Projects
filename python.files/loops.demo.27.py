"""

# 1 ile 100 arasındaki rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# ** "random " modülü için "python random" şeklinde arama yapın.
# ** 100 üzerinden puanlama yapın. Her soru 20 puan.
# ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen.

"""

import random

sayi = random.randint(1,100)            # 1,100 arasında bir sayı seçer.
can = int(input("Kac hak kullanmak istersiniz : "))
hak = can
sayac = 0

while (hak > 0):
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin :  "))

    if (sayi == tahmin):
        print(f"Tebrikler {sayac}. defada  bildiniz \o/  Toplam puanınız : {100 - ((100 / can) * (sayac - 1))}")
        break

    elif (sayi < tahmin):
        print("asagı")

    else:
        print("yukarı")


    if (hak == 0):
        print(f"Hakkınız bitti. Tutulan sayı : {sayi}")

