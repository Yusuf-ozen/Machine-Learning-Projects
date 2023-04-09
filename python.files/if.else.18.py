#1 - Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip  ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alabime koşulunu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

"""

isim = input("isim :  ")
yas = int(input("yas :  "))
egitim = input("egitim :  ")

if (yas >= 18) and (egitim == "üniversite" or egitim == "lise"):
    print("Ehliyet alabilirsiniz.")

else:
    print("no ehliyet")

"""


# Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
#  karşılık gelen not bilgisini yazdırın.
# 0 - 24 => 0
# 25 - 44 => 1
# 45 - 54 => 2
# 55 - 69 => 3
# 70 - 84 => 4
# 85 - 100 => 5
"""

mark1 = int(input("Mark 1 :  "))
mark2 = int(input("Mark 2 :  "))
mark3 = int(input("Mark 3 :  "))

Average = (mark1 + mark2 + mark3) / 3
print(f"Your average : {Average}")

if (Average > 0 and Average <= 24):
    print("Your grade : 0")

elif (Average >= 25 and Average <= 44):
    print("Your grade : 1")

elif (Average >= 45 and Average <= 54):
    print("Your grade : 2")

elif (Average >= 55 and Average <= 69):
    print("Your grade : 3")

elif (Average >= 70 and Average <= 84):
    print("Your grade : 4")


elif (Average >= 85 and Average <= 100):
    print("Your grade : 5")

else:
    print("invalid marks!")

"""


# day = int(input("Enter day which your car start traffic :   "))
# month = int(input("Enter month which your car start traffic :   "))
# year = int(input("Enter year which your car start traffic :   "))

# sum = ((2001 - year) * 365) + (month * 30) + (day)

# if (sum > 0) and (sum <= 365):
#     print("The first year")

# elif (sum >= 366) and (sum <= 730):
#     print("The second year")

# elif (sum >= 731) and (sum <= 1095):
#     print("The third year")

# else:
#     print("more than three years")



import datetime

tarih = (input("Aracınız hangi tarihte trafiğe çıkmıştır?(2019/08/09  :    "))

tarih = tarih.split(".")      # istersen "/" ya da "." ile yazmak istersen tarihi.
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

simdi = datetime.datetime.now()          # Bugünün tarihini alır ve gösterir.

fark = simdi - trafigeCikis  

print(fark)

days = fark.days                              #  print(fark.days)        # sadece sayısal olarak günü belirtir.


if (days <= 365):
    print("Birinci yıl")

elif (days > 365) and (days <= 365*2):
    print("ikinci yıl")

elif (days > 365 * 2) and (days <= 365 * 3):
    print("Ucuncu yil")

else:
    print("servis aralığı üç yıldan fazla")







