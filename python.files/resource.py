# def greeting(name):
#     print('hello', name)





# print(greeting('Yusuf'))
# print(greeting)


# sayHello = greeting

# print(sayHello)

# print(greeting)

# print(greeting('Ali'))
# print(sayHello('Ahmet'))







# # encapsulation

# def outer(num1):

#     print('outer')

#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1

#     num2 = inner_increment(num1)

#     print(num1, num2)


# outer(10)
# # innner_increment(10)  >> çalıştırmaz çünkü sadece 2.fonksiyonu kapsar.








# def factorial(number):

#     if not isinstance(number, int):
#         raise TypeError('Number must be an integer variable!')

#     if not number >= 0:
#         raise ValueError('Number must be more than zero')

#     def inner_factorial(number):

#         if number <= 1:
#             return 1


#         return number * inner_factorial(number - 1)

#     return inner_factorial(number)




# print(factorial(21))




















########    RETURNING    #########






# def us_alma(number):
    

#     def inner(power):
#         return number ** power


#     return inner



# two = us_alma(2)
# three = us_alma(3)

# print(two(2))
# print(three(5))







# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'admin':
#             return "{0} rolunun {1} sayfasına ulasabilir. ".format(role, page)

#         else:
#             return "{0} rolunun {1} sayfasına ulasamaz. ".format(role, page)

#     return inner


# user1 = yetki_sorgula('Product Edit')



# print(user1('admin'))
# print(user1('user'))










def islem(islem_adi):
    def toplam(*args):
        toplam = 0

        for i in args:
            toplam += i

        return toplam



    def carpim(*args):
        carpim = 1

        for i in args:
            carpim *= i

        return carpim


    if islem_adi == 'toplama':
        return toplam

    else:
        return carpim




toplama = islem('toplama')    ## toplama disinda bir sey yazarsan carpar.
print(toplama(1,3,5,6))


carpma = islem('carpma')
print(carpma(2,3,4,5,8))















