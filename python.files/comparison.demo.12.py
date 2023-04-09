




# 1 - Girilen 2 sayıdan büyük olanı hangisidir?

# a = int(input("Enter first number:  "))
# b = int(input("Enter second number:  "))

# result = (a > b)

# print(f"{a} büyüktür {b} ' den  : {result}")






# 2 - Kullanıcıdan 2 vize(%60) ve final(%40) isteyip ortalamayı hesaplayınız. 
# Eğer ortalama 50 ve üstüyse "geçti" değilse "Kaldı" yazınız.
"""
a = float(input("first exam :  "))
b = float(input("second exam :  "))
c = float(input("final exam :  "))

ave = ((a + b) * 0.3) + (c * 0.4)
result = (ave > 50)
print(f"Not ortalamnız : {ave} ve sınavı geçme durumunuz : {result}")
"""




# 3 - Girilen bir sayının tek mi çift mi olduğuna yazdırın.
"""
a = int(input("Number :  "))

result = (a % 2 == 0)
print(f"{a} nın çift olma durumu : {result}")

"""


# 4 - Girilen bir sayının negatif pozitif olduğunu yazdırın.
"""
a = int(input("Number :   "))

result = (a > 0)
print(f"{a} nın pozitif olma durumu : {result}")

"""


# 5 - Parola ve email bigisini alıp doğruluğunu kontrol ediniz.
# (email : email@sadıkturan.com , password : 123)

email = input("Enter email :  ")
password = int(input("Enter password :  "))

a = "email@sadıkturan.com"
b = 123

result = (a == email)
print(f"Yazdığınız    {email}    in doğruluğu : {result}")

res = (b == password)
print(f"Girdiğiniz    {password}    un doğruluğu : {res}")



