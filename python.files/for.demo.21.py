sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1 - Sayılar listesindeki hangi sayılar 3 ' ün katıdır?

for tek in sayilar:
    if (tek % 3 == 0):
        print(tek)


# 2 - Sayılar listesindeki sayıların toplamı kaçtır?

toplam = 0
for top in sayilar:
    toplam += top 

print("toplam : ",toplam)



# 3 - Sayılar listesindeki tek sayıların karesini alınız.

for tek in sayilar:
    if (tek % 2 == 1):

        print("karesi : ", tek ** 2)



sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]


# 4 - Şehirlerden hangileri en fazla 5 karakterlidir?

for sehir in sehirler:
    if (len(sehir) <= 5):           # harf sayısı 5' e eşit veya 5 den küçükse yazdırır.
        print(sehir)





urunler = [

    {"name" : "samsung S6", "price" : "3000" },
    {"name" : "samsung S7", "price" : "4000" },
    {"name" : "samsung S8", "price" : "5000" },
    {"name" : "samsung S9", "price" : "6000" },
    {"name" : "samsung S10", "price" : "7000" }
]



# 5 - Urunlerin fiyatları toplamı kaçtır?

top = 0

for urun in urunler:
    fiyat = int(urun["price"])           # string olan ifadeyi integer ' a çeviriyoruz.

    top += fiyat

print(top)



# 6 - Ürünlerden fiyatı en fazla 5000 olanları gösteriniz.

for urun in urunler:
 

     if (int(urun["price"]) <= 5000) :     # Burada fiyatı karşılaştrıp ürünün ismini yazdırırsın.
         print(urun["name"])




