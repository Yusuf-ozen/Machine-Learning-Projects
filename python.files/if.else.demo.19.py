# 1 - Girilen bir sayının 0 ile 100 arasında olduğunu kontrol ediniz.
"""

num = int(input("Enter a number :   "))

if (num > 0) and (num <= 100):
    print("Correct :)")

else:
    print("False :(") 

"""

# 2 - Girilen sayının pozitif çift sayı olduğunu belirtiniz.

"""

num = int(input("Enter a number :  "))

if (num > 0):

    if (num % 2 == 0):
        print("This number positive and even number")

    else:
        print("This number positive but odd number")


else:
    print("This number negative")

"""




# 3 - Email ve parola bilgileri ile giriş yapalım.

"""

email = "yusuf@"
password = "123"

a = input("Enter email :  ")
b = input("Enter password :  ")


if (a == email):
    if(b == password):
        print("Your email and password are true")

    else:
        print("Your email is true but password is wrong!")

else:
    if(b == password):
        print("Your password is true but email is wrong!")

    else:
        print("Your email and password are wrong")

"""


# 4 - Girilen 3 sayıyı büyüklük olarak karşılaştırın.
"""

a = int(input("First number :  "))
b = int(input("Second number :  "))
c = int(input("Third number :  "))

if (a > b) and (a > c):
    if (b > c):
        print(f"{a} > {b} > {c}")

    elif (c > b):
        print(f"{a} > {c} > {b}")

    else:
        print(f"{c} > {a} = {b}")


elif (b > a) and (b > c):
    if (a > c):
        print(f"{b} > {a} > {c}")

    elif (c > a):
        print(f"{b} > {c} > {a}")

    else:
        print(f"{b} > {a} = {c}   ")

    
elif (c > b) and (c > a):
    if (b > a):
        print(f"{c} > {b} > {a}")

    elif (a > b):
        print(f"{c} > {a} > {b}")

    else:
        print(f"{c} > {a} = {b}  ")


else:
    print(f"{a} = {b} = {c} ")
        

"""



# 5 - Kullanıcıdan 2 vize(%60) ve final(%40) isteyip ortalamayı hesaplayınız.
# Eğer ortalama 50 ve üstüyse geçti değilse kalsın.
#    a - Ortalama 50 ve üstü  bile olsa finalden 70 alması gerekir.
#    b - Finalden 70 alındığında ortalamanın bir önemi kalmasın.

"""
a = int(input("First exam :  "))
b = int(input("Second exam :  "))
c = int(input("Final exam :  "))

average = ((a + b) * 0.3) + (c * 0.4)

print(average)


if (c > 70):
    
    if (average >= 50):
        print("You have succeed :)")
    else:
        print("Your average low !")

else:
    if(average >= 50):
        print("Your Final mark is bad !!")

    else:
        print("Your average and Final grade low :((")

"""

# Kişinin ad, boy ve kilo bilgilerini alıp kilo indexlerini hesaplayınız.
#  Formül = kilo / boy uzunluğunun karesi
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir?

# 0 - 18.4  => zayıf
# 18.5 - 24.9 => normal
# 25.0 - 29.9 => fazla kilolu
# 30.0 - 34.9 => obez 


name = input("Enter name :  ")
weight = float(input("Enter weight :  "))
height = float(input("Enter height :  "))

index = weight / (height ** 2)

print(name)
print(index)

if (index > 0) and (index <= 18.4):
    print("ZAYIF")

elif (index >= 18.5) and (index <= 24.9):
    print("NORMAL")

elif (index >= 25.0) and (index <= 29.9):
    print("FAZLA KİLOLU")

elif (index >= 30.0) and (index <= 34.9):
    print("OBEZ")

else:
    print("out of the range")
