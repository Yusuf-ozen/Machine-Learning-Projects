"""

def square(num):  return num ** 2

numbers = [1, 3, 5]

result = list(map(square, numbers))                # 'map'  tüm liste elemanlarına ulaşır ve hepsinin karesini almayı sağlar. 

# result = square(2)


for item in map(square, numbers):             # Ayrıca böyle de yazdırabilirsin listeyi.
    print(item)  




print(result)

"""


"""

square = lambda num : num ** 2          # lambda yı isim vererek ayrı bir fonksiyon olarak da kullanabilirsin.

numbers = [1, 3, 5]

# result = list(map(lambda num : num ** 2 , numbers))                # 'lambda'  fonksiyon olmaksızın sayılara ne yapmak istediğini yazdırır. 
result = list(map(square, numbers))     


print(result)

"""


square = lambda num : num ** 2

numbers = [1, 3, 5, 6, 4, 9, 22]


# def checkEven(num):  return num % 2 == 0

checkEven = lambda num : num % 2 == 0


# result = list(filter(checkEven, numbers))
# result = list(filter(lambda num : num % 2 == 0, numbers))
result = list(filter(checkEven, numbers))


print(result)

