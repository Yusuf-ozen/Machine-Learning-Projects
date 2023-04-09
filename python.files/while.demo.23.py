sayilar = [1, 3, 5, 7, 9, 12, 19, 21]


# 1 - sayilar listesini while ile ekrana yazdıralim.
"""
i = 0

while (i < len(sayilar)):      # i yi arttırıp sıra sıra elemanları yazdırır.
    print(sayilar[i])
    i += 1

"""


# 2 - Baslangıç ve bitiş değerlerini alıp aradaki tüm tek sayilari ekrana yazdırın.
"""

first = int(input("Enter First number range :  "))
second = int(input("Enter Second number range :  "))
i = first

while (i <= second):
    if (i % 2 == 1):
        print(i)
    i += 1

"""

# 3 - 1 ile 100 arasındaki sayıları azalan şekilde yazdırın.
"""

i = 100
while (i >= 1):
    print(i)
    i -= 1

"""
# 4 - Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı olacak şekilde yazdırın.
"""

numbers = []     # numbers dizisi oluşturulur.
i = 0

while i < 5:
    sayi = int(input("Sayi :  "))      # sayi yi i = 5 olana kadar sorar.
    numbers.append(sayi)                # sayıları dizi içinde sıralar.
    i += 1
numbers.sort()          # sayilari küçükten büyüğe doğru sıralar.

print(numbers)

"""



# 5 - Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesine atınız.
#   ** Ürün sayısını kullanıcıya sorun.
#   ** Dictionary yapısına göre olsun. (name , price)
#   ** Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.


urunler = []

adet = int(input("kaç ürün girmek istiyorsunuz :  "))

i = 0

while i < adet:
    name = input("ürün ismi :  ")
    price = int(input("fiyatı giriniz :  "))

    urunler.append({
        "name" : name,        # her diziye karşılık gelecek olanı yazıyoruz.
        "price" : price

    })

    i += 1


for urun in urunler:
    print(f" urun adı : {name}  urun fiyatı : {price}")

