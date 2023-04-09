# 1 - Girilen bir sayının 0 ile 100 arasında olduğunu kontrol ediniz.
"""

a = int(input("Enter a number :  "))

result = (a < 100) and (a > 0)
print(result)

"""

# 2 - Girilen sayının pozitif çift sayı olup olmadığını kontrol edelim. 
"""

a = int(input("Enter a number :  "))

result = (a > 0) and (a % 2 == 0)

print(result)

"""

# 3 - Email ve parola bilgileri ile giriş yapalım.
"""

email = "@gmail"
password = 135

a = input("Enter email :  ")
b = int(input("Enter password :  "))

result = (a == email) and (b == password)
print (f"Yazdığınız {a} ve {b} nin doğruluğu : {result}")

"""

# 4 - Girilen 3 sayıyı büyüklük olarak karşılaştırın.
"""

a = int(input("Enter First Number :  "))
b = int(input("Enter Second Number :  "))
c = int(input("Enter Third Number :  "))

result = (a > b) and (a > c)
print(f"{a}  en büyüktür : {result}")

result = (b > a) and (b > c)
print(f"{b} en büyüktür : {result}")

result = (c > a) and (c > b)
print(f"{c} en büyüktür : {result}")

"""

# 5 - Kullanıcıdan 2 vize(%60) ve final(%40) isteyip ortalamayı hesaplayınız.
# Eğer ortalama 50 ve üstüyse geçti değilse kalsın.
#    a - Ortalama 50 ve üstü  bile olsa finalden 70 alması gerekir.
#    b - Finalden 70 alındığında ortalamanın bir önemi kalmasın.



# a = int(input("first exam :   "))
# b = int(input("second exam :   "))
# c = int(input("final exam :   "))

# Total = ((a + b) * 0.3) + (c * 0.4)

# result = (Total >= 50) and (c > 70)
# print(f"ortalamanız : {Total} ve geçem durumunuz : {result}")

"""

a = int(input("first exam :   "))
b = int(input("second exam :   "))
c = int(input("final exam :   "))

Total = ((a + b) * 0.3) + (c * 0.4)

result = (c > 70)
print(f"Ortalamanız  :  {Total}   sınıfı geçme durumu : {result}")

"""


# Kişinin ad, boy ve kilo bilgilerini alıp kilo indexlerini hesaplayınız.
#  Formül = kilo / boy uzunluğunun karesi
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir?

# 0 - 18.4  => zayıf
# 18.5 - 24.9 => normal
# 25.0 - 29.9 => fazla kilolu
# 30.0 - 34.9 => obez 


name = input("Enter name :  ")
a = float(input("Enter weight  :  "))
b = float(input("Enter height  :  "))

index = a / (b ** 2)


result = (index > 0) and (index <= 18.4)
print(f"Sir {name} Your index : {index} and you are thin : {result}")


result = (index >= 18.5) and (index <= 24.9)
print(f"Sir {name} Your index : {index} and you are normal : {result}")


result = (index >= 25.0) and (index <= 29.9)
print(f"Sir {name} Your index : {index} and you are fat : {result}")


result = (index >= 30.0) and (index <= 34.9)
print(f"Sir {name} Your index : {index} and you are overweight : {result}")




