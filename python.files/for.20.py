numbers = [1, 2, 3, 4, 5]


for num in numbers:            # "num" deyip ayrı bir değişken olarak veriyoruz.
    print(num)                 # listenin eleman sayısı kadar for döngüsü döner.



names = ["cınar", "sadık", "sena"]

for name in names:
    print(f"My name is {name}")          # tüm isimler için my name is kullanır.



ad = "Yusuf"

for a in ad:                 # yazılan tüm harfleri alt alta yazdırır.
    print(a)            



tuple = (1, 2, 3, 4, 5)       

for t in tuple:                  # tuple içindeki sayıları alt alta yazdırır.
    print(t)




tuple = ((1, 2), (3, 4), (5, 6))      # her bir parantezdeki gibi yazılıp alt alta yazdırılır.

for tu in tuple:
    print(tu)



tuple = ((1, 2), (3, 4), (5, 6))      # her bir parantezdeki gibi yazılıp alt alta yazdırılır.

for x,y in tuple:                    # sadece x'e karşılık gelenleri yazdırır.
    print(x)




tuple = ((1,2,3), (4,5,6), (7,8,9))

for a,b,c in tuple:                 # burada hangilerine karşılık gelenleri yazdırmak istersen onları printlersin.
    print(a,b)


d = {"k1" : 2, "k2" : 4, "k3" : 8}            # dictionary dizisi. (key => value)

for item in d:                                 # burda sadece key bilgilerine ulaşırız.
    print(item)


d = {"k1" : 1, "k2" : 2, "k3" : 3} 

for key,value in d.items():                     # burada hem key bilgilerini hem de value değerlerini yazdrır.
    print(key, value)






