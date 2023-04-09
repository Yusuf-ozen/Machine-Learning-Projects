# YONTEM 1

# import math

# import math as islem          # math'i islem takma ismiyle çağırıyoruz.


# # # value = dir(math)    # math modülündeki bütün bileşenleri value'ya attık.
# # # value = help(math)   # Buradaki help bilgi sahibi olmak için kullanılır.

# # # value = help(math.factorial)       # Burada math deki factorial hakkında bilgi sahibi olmak için yazılır.



# # value = math.sqrt(78)
# # value = math.factorial(34)
# # value = math.floor(9.88)
# # value = math.ceil(9.98)


# value = islem.factorial(12)
# value = islem.pow(100,100)

# print(value)



# YONTEM 2


# from math import *            # Bu sayede math'i yazmayıp sadece fonksiyonun ismini yazıp kullanabiliriz.


def sqrt(x):
    print('x : ' + str(x))


from math import factorial,sqrt         #$ Böyle yazıldığında sadece istediğin fonksiyonları kullanır.


value = sqrt(9)

value = pow(9999, 9999)

print(value)

